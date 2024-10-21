package main

import (
	"bufio"
	"fmt"
	"os"
	"sync"

	"github.com/alexmullins/zip"   // 用于处理zip文件的库
	"github.com/bodgit/sevenzip"   // 用于处理7z文件的库
	"github.com/nwaples/rardecode" // 用于处理RAR文件的库
)

// 加载密码文件
func loadcrypto(passwordFilePath string) ([]string, error) {
	file, err := os.Open(passwordFilePath) // 打开密码文件
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var passwords []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		passwords = append(passwords, scanner.Text()) // 将每行密码加入到切片中
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return passwords, nil
}

// 破解zip文件
func Crackzip(zipFilePath string, passwords []string) {
	var wg sync.WaitGroup         // 并发控制
	found := make(chan string, 1) // 创建通道存储正确密码

	for _, password := range passwords {
		wg.Add(1) // 增加WaitGroup计数
		go func(pwd string) {
			defer wg.Done()

			// 尝试使用密码打开zip文件
			reader, err := zip.OpenReader(zipFilePath)
			if err != nil {
				fmt.Println("无法打开zip文件:", err)
				return
			}
			defer reader.Close()

			// 尝试解压每个文件
			for _, file := range reader.File {
				file.SetPassword(pwd)
				rc, err := file.Open()
				if err == nil {
					rc.Close()
					found <- pwd // 将正确的密码发送到通道
					return       // 找到密码后立即返回
				}
			}
		}(password) // 使用闭包传递当前密码
	}

	go func() {
		wg.Wait()    // 等待所有goroutine结束
		close(found) // 关闭通道
	}()

	if correctPassword, ok := <-found; ok {
		fmt.Println("找到正确的密码:", correctPassword)
	} else {
		fmt.Println("未找到正确的密码。")
	}
}

// 破解RAR文件
// 破解RAR文件
func Crackrar(rarFilePath string, passwords []string) {
	var wg sync.WaitGroup
	found := make(chan string, 1)

	for _, password := range passwords {
		wg.Add(1)
		go func(pwd string) {
			defer wg.Done()

			// 打开RAR文件
			file, err := os.Open(rarFilePath)
			if err != nil {
				fmt.Println("无法打开RAR文件:", err)
				return
			}
			defer file.Close()

			// 尝试解压RAR文件
			rarReader, err := rardecode.NewReader(file, pwd)
			if err != nil {
				return
			}

			// 尝试读取RAR文件内容（验证密码）
			buf := make([]byte, 1024)
			_, err = rarReader.Read(buf)
			if err == nil {
				found <- pwd // 密码正确，发送到通道
				return
			}
		}(password)
	}

	go func() {
		wg.Wait()
		close(found)
	}()

	if correctPassword, ok := <-found; ok {
		fmt.Println("找到正确的密码:", correctPassword)
	} else {
		fmt.Println("未找到正确的密码。")
	}
}

// 破解7z文件
func Crack7z(sevenZipFilePath string, passwords []string) {
	var wg sync.WaitGroup
	found := make(chan string, 1)

	for _, password := range passwords {
		wg.Add(1)
		go func(pwd string) {
			defer wg.Done()

			// 尝试打开7z文件 (这里传递文件路径)
			archive, err := sevenzip.OpenReader(sevenZipFilePath)
			if err != nil {
				fmt.Println("无法读取7z文件:", err)
				return
			}
			defer archive.Close()

			// 尝试用密码解压
			// 如果密码验证逻辑适用7z，则执行逻辑处理
			for _, file := range archive.File {
				rc, err := file.Open()
				if err == nil {
					rc.Close() // 成功打开表示密码正确
					found <- pwd
					return
				}
			}
		}(password)
	}

	go func() {
		wg.Wait()
		close(found)
	}()

	if correctPassword, ok := <-found; ok {
		fmt.Println("找到正确的密码:", correctPassword)
	} else {
		fmt.Println("未找到正确的密码。")
	}
}

func main() {
	fmt.Println("请输入密码文件路径:")
	var passwordFilePath string
	fmt.Scan(&passwordFilePath)

	// 加载密码列表
	passwords, err := loadcrypto(passwordFilePath)
	if err != nil {
		fmt.Println("无法加载密码文件:", err)
		return
	}

	fmt.Println("请选择要爆破的文件类型: 1. ZIP 2. RAR 3. 7z")
	var choice int
	fmt.Scan(&choice)

	switch choice {
	case 1:
		fmt.Println("请输入ZIP文件路径:")
		var zipFilePath string
		fmt.Scan(&zipFilePath)
		Crackzip(zipFilePath, passwords)
	case 2:
		fmt.Println("请输入RAR文件路径:")
		var rarFilePath string
		fmt.Scan(&rarFilePath)
		Crackrar(rarFilePath, passwords)
	case 3:
		fmt.Println("请输入7z文件路径:")
		var sevenZipFilePath string
		fmt.Scan(&sevenZipFilePath)
		Crack7z(sevenZipFilePath, passwords)
	default:
		fmt.Println("无效的选项。")
	}
}

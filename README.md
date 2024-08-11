# Static Site Generator

## 🌟 Introduction

In a world where the web is rapidly evolving, there remains a timeless need for simplicity, speed, and control over content. Enter the **Static Site Generator**, a project born out of the desire to empower creators, developers, and enthusiasts alike to build blazing-fast websites with the elegance of minimalism.

### 🛤️ The Journey

The web has come a long way from its humble beginnings. As it evolved, so did the tools we use to create it. From hand-coded HTML to complex frameworks, the pursuit of better user experiences has driven the industry to new heights. Yet, in this pursuit, we've often overlooked one simple truth: **not every website needs to be complex**.

This project began with a simple observation: modern websites are often over-engineered, burdened with unnecessary complexity. There was a need for a tool that could strip away the noise, leaving only what truly matters—content.

Imagine a place where your content takes center stage, where every byte serves a purpose, and where speed is not a luxury but a guarantee. This is the vision behind the Static Site Generator.

## 📸 Showcase of Static Site Generator Output

Here are some screenshots of the static site generator in action:

![Index Page](documents/index.png | width=200)
![Majesty Page](documents/majesty.png | width=200)
![Tolkien Page](documents/tolkien.png | width=200)
![Web Dev Basics Page](documents/web_dev_basics.png | width=200)
![Web Dev Tips Page](documents/web_dev_tips.png | width=200)


## 🚀 Why This Project?

- **Simplicity at its Core:** This project was created to bring back the simplicity of static websites, allowing developers to focus on what they do best—creating content.
- **Speed and Performance:** Static sites are inherently fast. No more waiting for servers to render your pages. With pre-rendered HTML, your site will load faster than ever.
- **Security and Reliability:** By eliminating the need for a database or server-side processing, static sites are less vulnerable to attacks, offering a more secure experience.
- **Effortless Deployment:** Deploy your static site anywhere—whether it's a traditional web host, a CDN, or a GitHub Pages repository.

## 🛠️ Features

- **Recursive File Copying:** Automatically copy all static assets to your public directory with a single command.
- **Markdown to HTML Conversion:** Convert your markdown files into beautifully structured HTML with support for headings, lists, code blocks, and more.
- **Customizable Templates:** Use your own HTML templates to design your site exactly the way you want it.
- **Logging and Debugging:** Get detailed logs of the files being processed, so you always know what's happening under the hood.

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/natejonesiii/static-site-generator.git
cd static-site-generator

pip install -r requirements.txt
```

## 🧩 Usage
- Place your static files (images, CSS, etc.) in the static directory.
- Write your content in Markdown and save it in the content directory.
- Run the main script to generate your site:
```
bash main.sh
```
- Your site will be generated in the public directory, ready to be deployed!

## 🛡️ Security
By design, static sites generated with this tool are highly secure. With no server-side code or databases to exploit, the attack surface is minimized, making your site resistant to common vulnerabilities.

## 🏗️ Future Enhancements
While this project already provides a solid foundation, there are several exciting features planned for future releases:

- **Live Preview:** Preview your site in real-time as you write content.
- **Automated Deployments:** Seamlessly deploy your site to popular hosting platforms with a single command.
- **Advanced Templating:** Add support for more complex templates and dynamic content generation.
- **Automated Templating:** Add support to create new links for index page to show new directories added and name them appropriately.

## 🧑‍💻 Contributing
Contributions are welcome! Whether it's fixing bugs, adding new features, or improving documentation, your help is invaluable. Please submit a pull request or open an issue to get started.

## 🎉 Acknowledgments
A big thank you to the boot.dev community for inspiring this project. The simplicity and power of static sites have been championed by many, and this project is a humble contribution to that legacy.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
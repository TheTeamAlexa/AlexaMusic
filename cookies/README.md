## **Using Cookies for Authentication**

### **Method: Netscape HTTP Cookie File**

To authenticate requests using cookies, follow these steps:

#### **1. Export Cookies in Netscape Format**  
Use a browser extension to export cookies in the **Netscape HTTP Cookie File** format:

- **Firefox:** [Get cookies.txt (Firefox Add-on)](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)
- **Chrome:** [Get cookies.txt (Chrome Extension)](https://chromewebstore.google.com/detail/get-cookiestxt-clean/ahmnmhfbokciafffnknlekllgcnafnie)

#### **2. Upload Cookies to BatBin Service**  
1. Go to **[BatBin](https://batbin.me)**.
2. Upload your `cookies.txt` file.
3. Copy the generated URL.

#### **3. Configure the Environment Variable**
Paste the BatBin URL into your **`COOKIES`** environment variable.

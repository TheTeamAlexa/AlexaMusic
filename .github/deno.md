# **🚀 Deno Installation Guide**

## **🐧 Install Deno on Ubuntu**

### **✅ Official Install Script (Recommended)**

```bash
curl -fsSL https://deno.land/install.sh | sh
```

---

### **🔧 Add Deno to PATH**
```bash
export DENO_INSTALL="$HOME/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"
```

---

### **🔍 Verify Installation**
```bash
deno --version
```

---

> [!IMPORTANT]
> ### Fix (If Unzip Error Occurs)
>```bash
>sudo apt install -y p7zip-full
>```
>
>#### Then Re-Run The Install Script.

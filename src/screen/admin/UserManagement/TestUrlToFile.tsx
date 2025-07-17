import React, { useEffect } from "react";

// Hàm tải ảnh và chuyển thành File
async function urlToFile(url: string, filename?: string): Promise<File> {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to fetch image: ${response.statusText}`);
  }

  const blob = await response.blob();
  const name = filename || url.split("/").pop() || "image.jpg";

  return new File([blob], name, { type: blob.type });
}

const TestUrlToFile: React.FC = () => {
  useEffect(() => {
    const test = async () => {
      try {
        const file = await urlToFile(
          "https://bme.hcmiu.edu.vn/wp-content/uploads/2023/09/image22.jpg"
        );

        console.log("✅ File created:", file);
        console.log("📄 Name:", file.name);
        console.log("📦 Size:", file.size);
        console.log("🧾 Type:", file.type);

        // Optional: upload lại lên server
        /*
        const formData = new FormData();
        formData.append("avatar", file);

        const res = await fetch("/api/upload", {
          method: "POST",
          body: formData,
        });
        const data = await res.json();
        console.log("Upload result:", data);
        */
      } catch (err) {
        console.error("❌ Error:", err);
      }
    };

    test();
  }, []);

  return <div>Check console for file info.</div>;
};

export default TestUrlToFile;

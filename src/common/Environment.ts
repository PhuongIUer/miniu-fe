// Environment.ts
const GITHUB_JSON_URL = "https://res.cloudinary.com/miniu2025/raw/upload/v1752864252/domain_e7pfdj.json";

const EnvironmentConfig = {
  NGROK_BASE_URL: "",
  API_ENDPOINTS: {
    USERS: "/users",
    PRODUCTS: "/products",
    ORDERS: "/orders"
  },
  isInitialized: false,
};

let initializationPromise: Promise<void> | null = null;

export async function initializeEnvironment() {
  if (!initializationPromise) {
    initializationPromise = (async () => {
      try {
        const response = await fetch(GITHUB_JSON_URL, {
          cache: 'no-store', // Bỏ qua cache, luôn fetch từ server
        });
        
        if (!response.ok) {
          throw new Error(`Failed to fetch config: ${response.status}`);
        }

        const data = await response.json();
        EnvironmentConfig.NGROK_BASE_URL = data.domain + "/api";
        EnvironmentConfig.isInitialized = true;
      } catch (error) {
        console.error("Lỗi khi fetch domain.json từ GitHub:", error);
        // Có thể thêm fallback URL nếu cần
        EnvironmentConfig.NGROK_BASE_URL = "/api"; // Fallback nếu fetch thất bại
        EnvironmentConfig.isInitialized = true; // Vẫn đánh dấu đã khởi tạo để ứng dụng không bị treo
        throw error; // Nếu muốn xử lý lỗi ở nơi gọi hàm
      }
    })();
  }
  return initializationPromise;
}

export default EnvironmentConfig;
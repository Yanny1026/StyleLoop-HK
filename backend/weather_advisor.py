# 1. 獲取香港天文台 (HKO) 的最新天氣數據 (RSS/JSON)
# 2. 提取當前溫度和濕度
# 3. 根據 StyleLoop HK 的邏輯給出穿搭建議：
#    - 如果濕度 > 85%：建議「透氣/麻質 (Linen)」衣物，避免穿皮草或易霉材質。
#    - 如果溫度 < 18°C：建議「層次穿搭 (Layering)」。
#    - 如果有雨：提醒從虛擬衣櫥挑選「防水外套」。

import requests

def get_weather_data():
    """
    從香港天文台 API 獲取最新天氣數據。
    返回包含溫度、濕度和降雨信息的字典。
    """
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # 提取溫度數據（平均值）
        temp_data = data.get('temperature', {}).get('data', [])
        temps = [item['value'] for item in temp_data if 'value' in item]
        avg_temp = sum(temps) / len(temps) if temps else None
        
        # 提取濕度數據（平均值）
        humidity_data = data.get('humidity', {}).get('data', [])
        humidities = [item['value'] for item in humidity_data if 'value' in item]
        avg_humidity = sum(humidities) / len(humidities) if humidities else None
        
        # 檢查是否有雨（降雨量 > 0）
        rainfall_data = data.get('rainfall', {}).get('data', [])
        is_raining = any(item.get('max', 0) > 0 for item in rainfall_data if 'max' in item)
        
        return {
            'temperature': avg_temp,
            'humidity': avg_humidity,
            'is_raining': is_raining
        }
    except requests.RequestException as e:
        print(f"獲取天氣數據時出錯: {e}")
        return None

def get_clothing_suggestions(weather_data):
    """
    根據天氣數據給出穿搭建議。
    """
    if not weather_data:
        return ["無法獲取天氣數據"]
    
    temp = weather_data['temperature']
    humidity = weather_data['humidity']
    is_raining = weather_data['is_raining']
    
    suggestions = []
    
    if humidity and humidity > 85:
        suggestions.append("建議穿透氣/麻質 (Linen) 衣物，避免穿皮草或易霉材質。")
    
    if temp and temp < 18:
        suggestions.append("建議層次穿搭 (Layering)。")
    
    if is_raining:
        suggestions.append("提醒從虛擬衣櫥挑選防水外套。")
    
    if not suggestions:
        suggestions.append("天氣宜人，隨意穿搭！")
    
    return suggestions

def main():
    print("正在獲取香港天文台最新天氣數據...")
    
    weather = get_weather_data()
    
    if weather:
        temp = weather['temperature']
        humidity = weather['humidity']
        is_raining = weather['is_raining']
        
        print(f"當前溫度: {temp:.1f}°C" if temp else "溫度數據不可用")
        print(f"當前濕度: {humidity:.1f}%" if humidity else "濕度數據不可用")
        print(f"是否有雨: {'是' if is_raining else '否'}")
        
        print("\n穿搭建議:")
        suggestions = get_clothing_suggestions(weather)
        
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("無法獲取天氣數據，請檢查網路連接。")

if __name__ == "__main__":
    main()
    
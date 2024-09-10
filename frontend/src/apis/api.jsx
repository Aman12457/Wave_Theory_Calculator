const base_url = "http://127.0.0.1:5000";

export const result_display = async (formData) => {
  const response = await fetch(`${base_url}/result_display`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  });
  const data = await response.json();
  return data;
};

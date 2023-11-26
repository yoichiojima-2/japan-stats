const fetch_features = async () => {
  const res = await fetch("http://localhost:8000/social_stats/features");
  const data = await res.json()
  console.log(data)
  return {"props": data}
}
export default fetch_features;
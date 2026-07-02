import uvicorn

if __name__ == "__main__":
    print("=" * 60)
    print("Starting AI Teacher Assistant Backend")
    print("=" * 60)
    print("Backend will be available at:")
    print("  - http://localhost:8000")
    print("  - http://127.0.0.1:8000")
    print("")
    print("Press CTRL+C to stop")
    print("=" * 60)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        access_log=True
    )

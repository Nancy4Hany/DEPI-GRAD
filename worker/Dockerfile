# app image
FROM mcr.microsoft.com/dotnet/runtime:7.0
WORKDIR /app
COPY ./publish .
ENTRYPOINT ["dotnet", "Worker.dll"]
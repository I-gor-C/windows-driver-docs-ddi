---
UID: NF:ntddk.PsGetHostSilo
title: PsGetHostSilo function
author: windows-driver-content
description: This routine returns the host silo.
old-location: kernel\psgethostsilo.htm
old-project: kernel
ms.assetid: 0B78562C-25DD-4CF2-9804-6DBEDE8B5F69
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: PsGetHostSilo, PsGetHostSilo routine [Kernel-Mode Driver Architecture], kernel.psgethostsilo, ntddk/PsGetHostSilo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddk.h
api_name:
-	PsGetHostSilo
product: Windows
targetos: Windows
req.typenames: WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# PsGetHostSilo function
This routine returns the host silo.

## Syntax

````
PESILO PsGetHostSilo(void);
````

## Parameters

This function has no parameters.

## Return Value

The host silo.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1607 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | ntddk.h |
| **Library** | NtosKrnl.exe |
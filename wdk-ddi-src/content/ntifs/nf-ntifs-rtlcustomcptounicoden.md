---
UID: NF:ntifs.RtlCustomCPToUnicodeN
title: RtlCustomCPToUnicodeN function
author: windows-driver-content
description: Reserved for system use.
old-location: ifsk\rtlcustomcptounicoden.htm
old-project: ifsk
ms.assetid: 8f29aca1-9d38-4c28-976f-64549767b303
ms.author: windowsdriverdev
ms.date: 2/7/2018
ms.keywords: RtlCustomCPToUnicodeN, rtlref_9b39575d-4ba4-49fa-9281-2858d3e2631d.xml, ifsk.rtlcustomcptounicoden, ntifs/RtlCustomCPToUnicodeN, RtlCustomCPToUnicodeN function [Installable File System Drivers]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntifs.h
apiname:
-	RtlCustomCPToUnicodeN
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# RtlCustomCPToUnicodeN function
The <b>RtlCustomCPToUnicodeN</b> routine is reserved for system use. See <a href="..\ntifs\nf-ntifs-rtlmultibytetounicoden.md">RtlMultiByteToUnicodeN</a> and <a href="..\ntifs\nf-ntifs-rtloemtounicoden.md">RtlOemToUnicodeN</a>.

## Syntax

````
  RtlCustomCPToUnicodeN(
    
);
````

## Parameters

`CustomCP`

TBD

`UnicodeString`

TBD

`MaxBytesInUnicodeString`

TBD

`BytesInUnicodeString`

TBD

`CustomCPString`

TBD

`BytesInCustomCPString`

TBD


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** | NtosKrnl.exe |
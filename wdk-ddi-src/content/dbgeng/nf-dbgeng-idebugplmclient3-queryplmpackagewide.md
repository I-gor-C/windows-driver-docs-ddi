---
UID: NF:dbgeng.IDebugPlmClient3.QueryPlmPackageWide
title: IDebugPlmClient3::QueryPlmPackageWide method
author: windows-driver-content
description: Query a Process Lifecycle Management (PLM) package.
old-location: debugger\idebugplmclient3_queryplmpackagewide.htm
old-project: debugger
ms.assetid: 29BAAEF9-5B69-4723-BC23-A8B668E2A867
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugPlmClient3, IDebugPlmClient3 interface [Windows Debugging], QueryPlmPackageWide method, IDebugPlmClient3::QueryPlmPackageWide, QueryPlmPackageWide method [Windows Debugging], QueryPlmPackageWide method [Windows Debugging], IDebugPlmClient3 interface, QueryPlmPackageWide,IDebugPlmClient3.QueryPlmPackageWide, dbgeng/IDebugPlmClient3::QueryPlmPackageWide, debugger.idebugplmclient3_queryplmpackagewide
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	dbgeng.h
api_name:
-	IDebugPlmClient3.QueryPlmPackageWide
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# IDebugPlmClient3::QueryPlmPackageWide method
Query a Process Lifecycle Management (PLM) package.

## Syntax

```
HRESULT QueryPlmPackageWide(
  ULONG64              Server,
  PCWSTR               PackageFullName,
  PDEBUG_OUTPUT_STREAM Stream
);
```

## Parameters

`Server`

The server of the package.

`PackageFullName`

A pointer to the package name.

`Stream`

A pointer to an output stream for results.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/5B0580FF-0829-406A-B511-C0CD91A08D5F">IDebugPlmClient3</a>
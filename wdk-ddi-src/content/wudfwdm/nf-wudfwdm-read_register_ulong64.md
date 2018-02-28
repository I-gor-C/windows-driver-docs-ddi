---
UID: NF:wudfwdm.READ_REGISTER_ULONG64
title: READ_REGISTER_ULONG64 function
author: windows-driver-content
description: The READ_REGISTER_ULONG64 function reads a ULONG64 value from the specified register address.
old-location: wdf\read_register_ulong64.htm
old-project: wdf
ms.assetid: D8AB8735-8909-463E-B10E-1FE5FD557FBB
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: READ_REGISTER_ULONG64, READ_REGISTER_ULONG64 function, umdf.read_register_ulong64, wdf.read_register_ulong64, wudfddi_hwaccess/READ_REGISTER_ULONG64
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfwdm.h
req.include-header: Wdm.h, Miniport.h, Wudfwdm.h
req.target-type: Desktop
req.target-min-winverclnt: 64-bit Windows
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
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
-	Wudfddi_hwaccess.h
api_name:
-	READ_REGISTER_ULONG64
product: Windows
targetos: Windows
req.typenames: PO_FX_PERF_STATE_UNIT, *PPO_FX_PERF_STATE_UNIT
req.product: Windows 10 or later.
---


# READ_REGISTER_ULONG64 function
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>READ_REGISTER_ULONG64</b> function reads a ULONG64 value from the specified register address.

## Syntax

````
ULONG64 READ_REGISTER_ULONG64(
  _In_ IWDFDevice3 *pDevice,
  _In_ PULONG64    Register
);
````

## Parameters

`Register`

A pointer to the register address, which must be a mapped range in memory space.


## Return Value

<b>READ_REGISTER_ULONG64</b> returns the ULONG64 value that is read from the specified port address.

## Remarks

For more information, see <a href="https://msdn.microsoft.com/A0640E60-B0DF-4CAD-B292-CC1875EF7F7D">Reading and Writing to Device Registers in UMDF 1.x Drivers</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | 64-bit Windows  |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.11 |
| **Header** | wudfwdm.h (include Wdm.h, Miniport.h, Wudfwdm.h) |
| **Library** | NtosKrnl.exe |
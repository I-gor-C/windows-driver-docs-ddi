---
UID: NF:wdfhwaccess.WDF_READ_REGISTER_USHORT
title: WDF_READ_REGISTER_USHORT function
author: windows-driver-content
description: The WDF_READ_REGISTER_USHORT function reads a USHORT value from the specified register address.
old-location: wdf\wdf_read_register_ushort.htm
old-project: wdf
ms.assetid: EC3D7812-4EAB-419D-B736-47AE148FC61C
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: WDF_READ_REGISTER_USHORT, WDF_READ_REGISTER_USHORT function, wdf.wdf_read_register_ushort, wdfhwaccess/WDF_READ_REGISTER_USHORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfhwaccess.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
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
-	HeaderDef
api_location:
-	Wdfhwaccess.h
api_name:
-	WDF_READ_REGISTER_USHORT
product:
- Windows
targetos: Windows
req.typenames: WDF_FILE_INFORMATION_CLASS, *PWDF_FILE_INFORMATION_CLASS
req.product: Windows 10 or later.
---


# WDF_READ_REGISTER_USHORT function
<p class="CCE_Message">[Applies to UMDF only]

The <b>WDF_READ_REGISTER_USHORT</b> function reads a USHORT value from the specified register address.

## Syntax

```
USHORT WDF_READ_REGISTER_USHORT(
  WDFDEVICE Device,
  PUSHORT   Register
);
```

## Parameters

`Device`

A handle to a framework device object.

`Register`

A pointer to the register address, which must be a mapped range in memory space.


## Return Value

<b>WDF_READ_REGISTER_USHORT</b> returns the USHORT value that is read from the specified port address.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1  |
| **Target Platform** | Universal |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfhwaccess.h |
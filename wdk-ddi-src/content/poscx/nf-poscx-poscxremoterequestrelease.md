---
UID: NF:poscx.PosCxRemoteRequestRelease
title: PosCxRemoteRequestRelease function
author: windows-driver-content
description: PosCxRemoteRequestRelease is called whenever a remote device asks for the device to release. This initiates claim negotiation.
old-location: pos\poscxremoterequestrelease.htm
old-project: pos
ms.assetid: 1755E30C-15F8-41A9-9F4C-26455C92B66A
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: PosCxRemoteRequestRelease function, pos.poscxremoterequestrelease, PosCxRemoteRequestRelease, poscx/PosCxRemoteRequestRelease
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: poscx.h
req.include-header: Poscx.h
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
-	poscx.h
apiname:
-	PosCxRemoteRequestRelease
product: Windows
targetos: Windows
req.typenames: POS_CX_EVENT_PRIORITY
req.product: Windows 10 or later.
---


# PosCxRemoteRequestRelease function
PosCxRemoteRequestRelease is called whenever a remote device asks for
      the device to release.  This initiates claim negotiation.

## Syntax

````
NTSTATUS PosCxRemoteRequestRelease(
  _In_ WDFDEVICE device,
  _In_ ULONG     deviceInterfaceTag
);
````

## Parameters

`device`

A handle to a framework device object that represents the device.

`deviceInterfaceTag`

The device interface that initiated the release request.


## Return Value

Possible return values are:
<table>
<tr>
<td><b>STATUS_SUCCESS</b></td>
<td>The device will now start resolving the remote request to release.</td>
</tr>
<tr>
<td><b>STATUS_DEVICE_NOT_READY</b></td>
<td>The PosCx library was not successfully initialized.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | poscx.h (include Poscx.h) |
| **Library** | NtosKrnl.exe |
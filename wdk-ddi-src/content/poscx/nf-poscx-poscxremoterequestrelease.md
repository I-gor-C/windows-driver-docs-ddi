---
UID: NF.poscx.PosCxRemoteRequestRelease
title: PosCxRemoteRequestRelease function
author: windows-driver-content
description: PosCxRemoteRequestRelease is called whenever a remote device asks for the device to release. This initiates claim negotiation.
old-location: pos\poscxremoterequestrelease.htm
old-project: pos
ms.assetid: 1755E30C-15F8-41A9-9F4C-26455C92B66A
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PosCxRemoteRequestRelease
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
req.alt-api: PosCxRemoteRequestRelease
req.alt-loc: poscx.h
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
req.product: Windows 10 or later.
---

# PosCxRemoteRequestRelease function



## -description
PosCxRemoteRequestRelease is called whenever a remote device asks for
      the device to release.  This initiates claim negotiation.



## -syntax

````
NTSTATUS PosCxRemoteRequestRelease(
  _In_ WDFDEVICE device,
  _In_ ULONG     deviceInterfaceTag
);
````


## -parameters

### -param device [in]

A handle to a framework device object that represents the device.


### -param deviceInterfaceTag [in]

The device interface that initiated the release request.


## -returns
Possible return values are:

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Product

</th>
<td width="70%">
Windows 10 or later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Poscx.h (include Poscx.h)</dt>
</dl>
</td>
</tr>
</table>
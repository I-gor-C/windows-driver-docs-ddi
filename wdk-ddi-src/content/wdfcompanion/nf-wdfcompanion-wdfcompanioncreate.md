---
UID: NF.wdfcompanion.WdfCompanionCreate
title: WdfCompanionCreate function
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdfcompanioncreate.htm
old-project: wdf
ms.assetid: 78b9eccf-34ef-40ae-b7fc-6fa8400f8c2a
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfCompanionCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcompanion.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.23
req.alt-api: WdfCompanionCreate
req.alt-loc: wdfcompanion.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfCompanionCreate function



## -description

			For internal use only.



## -syntax

````
NTSTATUS WdfCompanionCreate(
  _Inout_  PWDFDEVICE_INIT        *DeviceInit,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES DeviceAttributes,
  _Out_    WDFCOMPANION           *Companion
);
````


## -parameters

### -param DeviceInit [in, out]


### -param DeviceAttributes [in, optional]


### -param Companion [out]


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.23

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfcompanion.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>
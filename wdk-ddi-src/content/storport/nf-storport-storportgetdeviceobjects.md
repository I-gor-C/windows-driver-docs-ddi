---
UID: NF.storport.StorPortGetDeviceObjects
title: StorPortGetDeviceObjects
author: windows-driver-content
description: The StorPortGetDeviceObjects routine returns the device objects that are associated with the adapter device stack.
old-location: storage\storportgetdeviceobjects.htm
old-project: storage
ms.assetid: e48b5048-5f5f-4efb-b7bf-2dd183074516
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortGetDeviceObjects
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortGetDeviceObjects
req.alt-loc: storport.h
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
req.iface: 
req.product: Windows 10 or later.
---

# StorPortGetDeviceObjects function



## -description
<p>The <b>StorPortGetDeviceObjects</b> routine returns the device objects that are associated with the adapter device stack. The device objects that will be returned are the functional and physical device objects of the adapter and the device object to which the functional device object is attached. </p>


## -syntax

````
ULONG StorPortGetDeviceObjects(
  _In_  PVOID HwDeviceExtension,
  _Out_ PVOID *AdapterDeviceObject,
  _Out_ PVOID *PhysicalDeviceObject,
  _Out_ PVOID *LowerDeviceObject
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>AdapterDeviceObject</i> [out]

<dd>
<p>A pointer to receive the functional device object (FDO) of the adapter.</p>
</dd>

### -param <i>PhysicalDeviceObject</i> [out]

<dd>
<p>A pointer to receive the physical device object (PDO).</p>
</dd>

### -param <i>LowerDeviceObject</i> [out]

<dd>
<p>A pointer to receive the device object of lower device to which the FDO is attached.</p>
</dd>
</dl>

## -returns
<p><b>StorPortGetDeviceObjects</b> returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the device objects were obtained successfully.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>HwDeviceExtension</i> was <b>NULL</b>.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
</table>
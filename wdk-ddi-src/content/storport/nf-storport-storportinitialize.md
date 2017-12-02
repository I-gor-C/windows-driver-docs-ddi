---
UID: NF.storport.StorPortInitialize
title: StorPortInitialize
author: windows-driver-content
description: The StorPortInitilize routine initializes the port driver parameters and extension data. StorPortInitilize also saves the adapter information provided from the miniport driver.
old-location: storage\storportinitialize.htm
old-project: storage
ms.assetid: b560ce42-3c5c-4766-bb9c-6590b7113ecd
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortInitialize
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
req.alt-api: StorPortInitialize
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# StorPortInitialize function



## -description
<p>The <b>StorPortInitilize</b> routine initializes the port  driver parameters and extension data. <b>StorPortInitilize</b> also saves the adapter information provided from the miniport driver.</p>


## -syntax

````
STORPORT_API ULONG StorPortInitialize(
  _In_     PVOID                   Argument1,
  _In_     PVOID                   Argument2,
  _In_     PHW_INITIALIZATION_DATA HwInitializationData,
  _In_opt_ PVOID                   HwContext
);
````


## -parameters
<dl>

### -param Argument1 [in]

<dd>
<p>The first pointer with which the operating system called the miniport's <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine. </p>
</dd>

### -param Argument2 [in]

<dd>
<p>The second pointer with which the operating system called the miniports's <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine. </p>
</dd>

### -param HwInitializationData [in]

<dd>
<p>Pointer to the initialization and configuration information set by the miniport driver in it's <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine. </p>
</dd>

### -param HwContext [in, optional]

<dd>
<p>Is the address of a context value to be passed to the miniport driver's <a href="storage.hwstorfindadapter">HwStorFindAdapter</a> routine. Only legacy miniport drivers that scan the bus for HBAs rather than receiving configuration information from the port driver can use this parameter to store state between calls to <b>HwStorFindAdapter</b>. </p>
</dd>
</dl>

## -returns
<p>
      The result of the initialization actions performed by <b>StorPortInitilize</b>. The miniport driver will return this value as the return value for its <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine.</p>

<p><b>StorPortInitilize</b> returns one of the following status codes:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p><i>Argument1</i> is NULL.</p>

<p>-or-</p>

<p><i>Argument2</i> is NULL.</p>

<p>-or-</p>

<p><i>HwInitializationData</i> is NULL.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The driver extension data and adapter information were initialized successfully.</p><dl>
<dt><b> STATUS_NO_MEMORY</b></dt>
</dl><p>No memory is available to store an initialization parameter.</p><dl>
<dt><b> STATUS_REVISION_MISMATCH</b></dt>
</dl><p>The version of the structure pointed to by <i>HwInitializationData</i> is invalid for the current operating system.</p><dl>
<dt><b> STATUS_INSUFFICENT_RESOURCES</b></dt>
</dl><p>The allocation failed for the driver object extension data.</p>

<p> </p>

## -remarks
<p>This routine must be called from the miniport driver's <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine.</p>

<p>Because Storport miniport drivers must support PnP, the Storport driver does not use the <i>HwContext</i> parameter passed to <b>StorPortInitilize</b>.</p>

<p>Every miniport driver's <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine must call <b>StorPortInitilize</b> after the miniport driver has first zeroed and then set the members of <a href="storage.hw_initialization_data__storport_">HW_INITIALIZATION_DATA</a>.</p>

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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.hw_initialization_data__storport_">HW_INITIALIZATION_DATA</a>
</dt>
<dt>
<a href="storage.hwstorfindadapter">HwStorFindAdapter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortInitialize routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

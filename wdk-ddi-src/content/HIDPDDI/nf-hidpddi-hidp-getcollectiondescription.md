---
UID: NF.hidpddi.HidP_GetCollectionDescription
title: HidP_GetCollectionDescription
author: windows-driver-content
description: Fills a device description block with collection description and the corresponding report ID information for the specified report descriptor.
old-location: hid\hidp_getcollectiondescription.htm
ms.assetid: F8FD0C10-115D-4ACF-8C7F-127D342EA9CD
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: hid
req.header: hidpddi.h
req.include-header: Hidpddi.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HidP_GetCollectionDescription
req.alt-loc: Hidparse.lib,Hidparse.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hidparse.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: HidP_GetCollectionDescription
req.iface: 
---

# HidP_GetCollectionDescription function



## -description
<p>Fills a device description
    block with collection description and the corresponding 
    report ID information for the specified report descriptor. 
    A HID minidriver generally does not need to call this function. Instead, it returns the report descriptor to Hidclass driver in response to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541147">IOCTL_HID_GET_REPORT_DESCRIPTOR</a>.</p>


## -syntax

````
BOOLEAN __stdcall HidP_GetCollectionDescription(
  _In_  PHIDP_REPORT_DESCRIPTOR ReportDesc,
  _In_  ULONG                   DescLength,
  _In_  POOL_TYPE               PoolType,
  _Out_ PHIDP_DEVICE_DESC       DeviceDescription
);
````


## -parameters
<dl>

### -param <i>ReportDesc</i> [in]

<dd>
<p>A pointer to a UCHAR array that contains the raw report descriptor.</p>
</dd>

### -param <i>DescLength</i> [in]

<dd>
<p>The length of the report descriptor array.</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>-value that indicates the pool type from which memory for the linked list is allocated. This includes each <a href="https://msdn.microsoft.com/library/windows/hardware/mt740161">HIDP_COLLECTION_DESC</a> array element of <a href="https://msdn.microsoft.com/library/windows/hardware/mt740162">HIDP_DEVICE_DESC</a>, each <a href="hid._hidp_preparsed_data">HIDP_PREPARSED_DATA</a> in each <b>HIDP_COLLECTION_DESC</b>, each <a href="https://msdn.microsoft.com/library/windows/hardware/mt740165">HIDP_REPORT_IDS</a> array element of <b>HIDP_DEVICE_DESC</b>.</p>
</dd>

### -param <i>DeviceDescription</i> [out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt740162">HIDP_DEVICE_DESC</a> structure that is populated with device description block filled in
                         collection descriptors as linked lists. This is a caller-allocated structure. However, its <a href="https://msdn.microsoft.com/library/windows/hardware/mt740161">HIDP_COLLECTION_DESC</a> array elements and <a href="https://msdn.microsoft.com/library/windows/hardware/mt740165">HIDP_REPORT_IDS</a> array elements are allocated by this function.</p>
</dd>
</dl>

## -returns
<p><b>HidP_GetCollectionDescription</b> can return one of these values: <b>TRUE</b> if it successfully fills the device description block. Otherwise, it returns <b>FALSE</b>.</p><dl>
<dt>STATUS_SUCCESS</dt>
</dl><p>Successfully parsed
                                      the report descriptor and allocated the
                                      memory blocks necessary to describe the
                                      device.</p><dl>
<dt>STATUS_NO_DATA_DETECTED</dt>
</dl><p>Failed to find top-level collections
                                      in the report descriptor.</p><dl>
<dt>STATUS_COULD_NOT_INTERPRET       </dt>
</dl><p>An error was detected in the report 
                                      descriptor. See the error code in
                                      <b>Dbg</b> field of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt740162">HIDP_DEVICE_DESC</a> structure.</p><dl>
<dt>STATUS_BUFFER_TOO_SMALL</dt>
</dl><p>Found the end of the report descriptor
                                      when it expected more data.</p><dl>
<dt>STATUS_INSUFFICIENT_RESOURCES</dt>
</dl><p>Failed to allocate memory.</p><dl>
<dt>STATUS_ILLEGAL_INSTRUCTION</dt>
</dl><p>Failed to parse an an item in the report 
                                      descriptor.</p><dl>
<dt> HIDP_STATUS_INVALID_REPORT_TYPE</dt>
</dl><p>Report ID of 0 was found in the
                                      descriptor.</p>

<p> </p>

## -remarks
<p>    For a raw report descriptor that is specified by the <i>ReportDesc</i> parameter, <i>HidP_GetCollectionDescription</i> fills in the <i>DeviceDescription</i>
    block with a caller-allocated linked list of collection descriptors and the corresponding 
    Report ID information that is described by the given report descriptor. 
    The memory for the collection information and the ReportID information is
    allocated based on the <i>PoolType</i> value.
</p>

<p>    For a raw report descriptor that is specified by the <i>ReportDesc</i> parameter, <i>HidP_GetCollectionDescription</i> fills in the <i>DeviceDescription</i>
    block with a caller-allocated linked list of collection descriptors and the corresponding 
    Report ID information that is described by the given report descriptor. 
    The memory for the collection information and the ReportID information is
    allocated based on the <i>PoolType</i> value.
</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidpddi.h (include Hidpddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hidparse.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>
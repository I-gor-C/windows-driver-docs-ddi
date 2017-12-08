---
UID: NF.strmini.StreamClassGetPhysicalAddress
title: StreamClassGetPhysicalAddress function
author: windows-driver-content
description: The StreamClassGetPhysicalAddress routine translates a virtual memory address to a physical memory address and locks the corresponding physical memory for a DMA operation.
old-location: stream\streamclassgetphysicaladdress.htm
old-project: stream
ms.assetid: 5a8e7130-00e7-4bff-8939-7cfcc1a2b9aa
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: StreamClassGetPhysicalAddress
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StreamClassGetPhysicalAddress
req.alt-loc: Stream.lib,Stream.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Stream.lib
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# StreamClassGetPhysicalAddress function



## -description
The <b>StreamClassGetPhysicalAddress</b> routine translates a virtual memory address to a physical memory address and locks the corresponding physical memory for a DMA operation.


## -syntax

````
STREAM_PHYSICAL_ADDRESS StreamClassGetPhysicalAddress(
  _In_     PVOID                    HwDeviceExtension,
  _In_opt_ PHW_STREAM_REQUEST_BLOCK HwSRB,
  _In_     PVOID                    VirtualAddress,
  _In_     STREAM_BUFFER_TYPE       Type,
  _Out_    ULONG                    *Length
);
````


## -parameters

### -param HwDeviceExtension [in]

Pointer to the minidriver's device extension. The minidriver specifies the size of this buffer in the <a href="stream.hw_initialization_data">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="stream.streamclassregisterminidriver">StreamClassRegisterMinidriver</a>. The class driver then passes pointers to the buffer in the <b>HwDeviceExtension</b> member of the <a href="stream.hw_stream_request_block">HW_STREAM_REQUEST_BLOCK</a>, <a href="stream.hw_stream_object">HW_STREAM_OBJECT</a>, <a href="stream.hw_time_context">HW_TIME_CONTEXT</a>, and <a href="stream.port_configuration_information">PORT_CONFIGURATION_INFORMATION</a> structures it passes to the minidriver.

### -param HwSRB [in, optional]

Specifies a stream request block. This parameter is used only if the <i>Type</i> parameter has the value SRBDataBuffer, otherwise <i>HwSRB</i> should be <b>NULL</b>. This parameter is optional.  

### -param VirtualAddress [in]

Specifies the virtual address to be translated.

### -param Type [in]

Specifies the type of buffer pointed to by <i>VirtualAddress</i>. This value may be PerRequestExtension, DmaBuffer, or SRBDataBuffer.

### -param Length [out]

Specifies the length, in bytes, of the buffer.

## -returns
<b>StreamClassGetPhysicalAddress</b> returns the translated virtual address as a physical memory address.

## -remarks
The type of buffer to be used is specified in the <i>Type</i> parameter. The meanings of these values are shown in the following table.

PerRequestExtension

Indicates the physical address of the SRB extension.

DmaBuffer

Indicates the physical address of the DMA buffer.

SRBDataBuffer

Indicates the physical address of the data buffer.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Stream.lib</dt>
</dl>
</td>
</tr>
</table>
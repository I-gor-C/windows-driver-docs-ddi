---
UID: NF.dbgeng.IDebugDataSpaces4.ReadProcessorSystemData
title: IDebugDataSpaces4::ReadProcessorSystemData
author: windows-driver-content
description: The ReadProcessorSystemData method returns data about the specified processor.
old-location: debugger\readprocessorsystemdata.htm
old-project: debugger
ms.assetid: 8cb63fe6-61da-4c37-975d-d82430195863
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugDataSpaces4, ReadProcessorSystemData, IDebugDataSpaces4::ReadProcessorSystemData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces.ReadProcessorSystemData,IDebugDataSpaces2.ReadProcessorSystemData,IDebugDataSpaces3.ReadProcessorSystemData,IDebugDataSpaces4.ReadProcessorSystemData
req.alt-loc: dbgeng.h
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
req.iface: IDebugDataSpaces4
---

# IDebugDataSpaces4::ReadProcessorSystemData method



## -description
<p>The <b>ReadProcessorSystemData</b> method returns data about the specified processor.</p>


## -syntax

````
HRESULT ReadProcessorSystemData(
  [in]            ULONG  Processor,
  [in]            ULONG  Index,
  [out]           PVOID  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG DataSize
);
````


## -parameters
<dl>

### -param Processor [in]

<dd>
<p>Specifies the processor whose data is to be read.</p>
</dd>

### -param Index [in]

<dd>
<p>Specifies the data type to read.  The following table contains the valid values.  After successful completion, the data returned in the buffer <i>Buffer</i> has the type specified by the middle column.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KPCR_OFFSET</p>
</td>
<td>
<p>Returns the virtual address of the processor's Processor Control Region (PCR).</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PULONG64.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KPRCB_OFFSET</p>
</td>
<td>
<p>Returns the virtual address of the processor's Processor Control Block (PRCB).</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PULONG64.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_KTHREAD_OFFSET</p>
</td>
<td>
<p>Returns the virtual address of the KTHREAD structure for the system thread  running on the processor.</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PULONG64.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_BASE_TRANSLATION_VIRTUAL_OFFSET</p>
</td>
<td>
<p>Returns the virtual address of the base of the paging information owned by the operating system or the processor.  The address and the content at the address are processor- and operating-system-dependent. </p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PULONG64.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_PROCESSOR_IDENTIFICATION</p>
</td>
<td>
<p>Returns a description of the processor.</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PDEBUG_PROCESSOR_IDENTIFICATION_ALL .</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_DATA_PROCESSOR_SPEED</p>
</td>
<td>
<p>Returns the speed of the processor in MHz.  This may not work in a particular session.</p>
<p>In this case, the argument <i>Buffer</i> can be considered to have type PULONG.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param Buffer [out]

<dd>
<p>Receives the processor data.  Upon successful completion of the method, the contents of this buffer may be accessed by casting <i>Buffer</i> to the type specified in the above table.</p>
</dd>

### -param BufferSize [in]

<dd>
<p>Specifies the size in bytes of the buffer <i>Buffer</i>.  This is the maximum number of bytes that will be returned.</p>
</dd>

### -param DataSize [out, optional]

<dd>
<p>Receives the size of the data in bytes.  If <i>DataSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p>

## -remarks
<p>This method is only available in kernel-mode debugging.</p>

<p>For information about the PCR, PRCB, and KTHREAD structures, as well as information about paging tables, see <i>Microsoft Windows Internals</i> by David Solomon and Mark Russinovich.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>
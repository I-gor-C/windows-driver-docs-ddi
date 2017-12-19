---
UID: NF.wdm.KeFlushIoBuffers
title: KeFlushIoBuffers function
author: windows-driver-content
description: The KeFlushIoBuffers routine flushes the memory region described by an MDL from caches of all processors.
old-location: kernel\keflushiobuffers.htm
old-project: kernel
ms.assetid: 76954a20-7cd7-454b-a965-8c3f0cdb6e8f
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: KeFlushIoBuffers
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeFlushIoBuffers
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: MdlAfterReqCompletedIntIoctlA, MdlAfterReqCompletedIoctlA, MdlAfterReqCompletedReadA, MdlAfterReqCompletedWriteA
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# KeFlushIoBuffers function



## -description
The <b>KeFlushIoBuffers</b> routine flushes the memory region described by an MDL from caches of all processors.



## -syntax

````
VOID KeFlushIoBuffers(
  _In_ PMDL    Mdl,
  _In_ BOOLEAN ReadOperation,
  _In_ BOOLEAN DmaOperation
);
````


## -parameters

### -param Mdl [in]

A pointer to an MDL that describes the range for the I/O buffer.


### -param ReadOperation [in]

Specifies <b>TRUE</b> if the flush is being performed for a read operation, and <b>FALSE</b> for a write operation. For more information, see the following Remarks section.


### -param DmaOperation [in]

Specifies <b>TRUE</b> for a DMA transfer, <b>FALSE</b> for PIO.


## -returns
None


## -remarks
Drivers call <b>KeFlushIoBuffers</b> to maintain data integrity during DMA or PIO device transfer operations. Calling this routine affects all processors in the machine.

If <i>ReadOperation</i> is <b>TRUE</b>, the driver is reading information from the device to system memory, so valid data still might be in the processor instruction and data caches. <b>KeFlushIoBuffers</b> flushes data from all processors' caches to system memory, including the processor on which the caller is running.

If <i>ReadOperation</i> is <b>FALSE</b>, the driver is writing data from system memory to a device, so valid data might be in the processor's data cache but not yet transferred to the device. <b>KeFlushIoBuffers</b> flushes all processors' data caches, including that of the processor on which the caller is running.

As a general rule, drivers should call <b>KeFlushIoBuffers</b> just before beginning a DMA transfer operation or immediately following any PIO read operation.

<b>KeFlushIoBuffers</b> flushes only the memory region that is described by the MDL that the <i>Mdl</i> parameter points to. To flush all the memory regions that are described by an MDL chain requires a separate <b>KeFlushIoBuffers</b> call for each MDL in the chain.

For more information, see the following topics:


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_mdlafterreqcompletedintioctla">MdlAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_mdlafterreqcompletedioctla">MdlAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_mdlafterreqcompletedreada">MdlAfterReqCompletedReadA</a>, <a href="devtest.kmdf_mdlafterreqcompletedwritea">MdlAfterReqCompletedWriteA</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nc-wdm-pflush_adapter_buffers.md">FlushAdapterBuffers</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeFlushIoBuffers routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


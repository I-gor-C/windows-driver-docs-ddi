---
UID: NF.wdm.IoWMIQuerySingleInstanceMultiple
title: IoWMIQuerySingleInstanceMultiple
author: windows-driver-content
description: The IoWMIQuerySingleInstanceMultiple routine returns all WMI data block instances that implement the specified WMI classes with the specified instance names.
old-location: kernel\iowmiquerysingleinstancemultiple.htm
old-project: kernel
ms.assetid: c0e011b5-804c-4f0d-a125-a083a0f83d50
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoWMIQuerySingleInstanceMultiple
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoWMIQuerySingleInstanceMultiple
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoWMIQuerySingleInstanceMultiple function



## -description
<p>The <b>IoWMIQuerySingleInstanceMultiple</b> routine returns all WMI data block instances that implement the specified WMI classes with the specified instance names.</p>


## -syntax

````
NTSTATUS IoWMIQuerySingleInstanceMultiple(
  _In_      PVOID           *DataBlockObjectList,
  _In_      PUNICODE_STRING InstanceNames,
  _In_      ULONG           ObjectCount,
  _Inout_   ULONG           *InOutBufferSize,
  _Out_opt_ PVOID           OutBuffer
);
````


## -parameters
<dl>

### -param <i>DataBlockObjectList</i> [in]

<dd>
<p>Pointer to an array of pointers of WMI data block objects. The caller opens a data block object for each WMI class with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550453">IoWMIOpenBlock</a> routine. Each object must be opened with the WMIGUID_QUERY access right.</p>
</dd>

### -param <i>InstanceNames</i> [in]

<dd>
<p>Pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structures containing instance names. The <i>n</i>th instance name in the array corresponds to the value of the <b>InstanceName</b> property for the <i>n</i>th WMI class specified in the array pointed to by the <i>DataBlockObjectList</i> parameter.</p>
</dd>

### -param <i>ObjectCount</i> [in]

<dd>
<p>Specifies the number of entries in the arrays passed in the <i>DataBlockObjectList</i> and <i>InstanceNames</i> parameters. </p>
</dd>

### -param <i>InOutBufferSize</i> [in, out]

<dd>
<p>Pointer to a memory location that specifies the size of the buffer passed in the <i>OutBuffer</i> parameter. If the routine succeeds, it updates the memory location to specify the number of bytes actually stored in <i>OutBuffer</i>. If the routine fails with STATUS_BUFFER_TOO_SMALL, it returns the number of bytes required to return the data.</p>
</dd>

### -param <i>OutBuffer</i> [out, optional]

<dd>
<p>Pointer to the buffer where the routine returns the WMI data. The routine returns a sequence of variable-sized <a href="https://msdn.microsoft.com/library/windows/hardware/ff566377">WNODE_SINGLE_INSTANCE</a> structures, one for each data block instance. The <b>WnodeHeader.Linkage</b> member of each <b>WNODE_SINGLE_INSTANCE</b> structure contains the offset from the beginning of the current <b>WNODE_SINGLE_INSTANCE</b> to the beginning of the next <b>WNODE_SINGLE_INSTANCE</b>. The final block in the chain has <b>WnodeHeader.Linkage</b> set to zero. Each distinct data block instance corresponds to a single matching WMI class and instance name. <i>OutBuffer</i> must point to a buffer allocated from nonpaged pool. </p>
</dd>
</dl>

## -returns
<p>The routine returns an NTSTATUS code. Possible return values include:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation succeeded. The routine returns the WMI data in the buffer pointed to by the <i>OutBuffer</i> parameter. The routine also returns the size, in bytes, of the returned data in the memory location pointed to by the <i>InOutBufferSize</i> parameter.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer passed by the caller in the <i>OutBuffer</i> parameter is too small. The routine returns the required buffer size in the memory location pointed to by the <i>InOutBufferSize</i> parameter.</p>

<p> </p>

## -remarks
<p><b>IoWMIQuerySingleInstanceMultiple</b> determines which drivers might support the specified WMI classes and instance names, and issues an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551718">IRP_MN_QUERY_SINGLE_INSTANCE</a> request to each such driver. Each driver that exports the data block instance with matching <b>InstanceName</b> property returns the appropriate data.</p>

<p>If no drivers implement any of the specified WMI classes and instance names, the routine returns STATUS_SUCCESS. It also returns a value of zero in the memory location pointed to by the <i>InOutBufferSize</i> parameter.</p>

<p>To query for a single WMI class and instance name, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550471">IoWMIQuerySingleInstance</a> routine. Drivers can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550493">IoWMISetSingleInstance</a> routine to update a class instance.</p>

<p><b>IoWMIQuerySingleInstanceMultiple</b> determines which drivers might support the specified WMI classes and instance names, and issues an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551718">IRP_MN_QUERY_SINGLE_INSTANCE</a> request to each such driver. Each driver that exports the data block instance with matching <b>InstanceName</b> property returns the appropriate data.</p>

<p>If no drivers implement any of the specified WMI classes and instance names, the routine returns STATUS_SUCCESS. It also returns a value of zero in the memory location pointed to by the <i>InOutBufferSize</i> parameter.</p>

<p>To query for a single WMI class and instance name, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550471">IoWMIQuerySingleInstance</a> routine. Drivers can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550493">IoWMISetSingleInstance</a> routine to update a class instance.</p>

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
<p>Available in Windows XP and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550453">IoWMIOpenBlock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550471">IoWMIQuerySingleInstance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550493">IoWMISetSingleInstance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551718">IRP_MN_QUERY_SINGLE_INSTANCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWMIQuerySingleInstanceMultiple routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

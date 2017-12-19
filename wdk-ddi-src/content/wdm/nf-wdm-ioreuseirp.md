---
UID: NF.wdm.IoReuseIrp
title: IoReuseIrp function
author: windows-driver-content
description: The IoReuseIrp routine reinitializes an IRP so that it can be reused.
old-location: kernel\ioreuseirp.htm
old-project: kernel
ms.assetid: 18ad2c76-110f-45a9-986b-67e7c81f256f
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IoReuseIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoReuseIrp
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IoReuseIrp, IoReuseIrp2, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# IoReuseIrp function



## -description
The <b>IoReuseIrp</b> routine reinitializes an IRP so that it can be reused.



## -syntax

````
VOID IoReuseIrp(
  _Inout_ PIRP     Irp,
  _In_    NTSTATUS Status
);
````


## -parameters

### -param Irp [in, out]

Pointer to the IRP to be reinitialized for reuse. 


### -param Status [in]

Specifies the NTSTATUS value to be set in the IRP after it is reinitialized.


## -returns
None


## -remarks
Drivers for Windows 2000 and later versions of Windows use <b>IoReuseIrp</b> to reuse an IRP.

A driver should use <b>IoReuseIrp</b> only on IRPs it previously allocated either as raw memory or with <a href="kernel.ioallocateirp">IoAllocateIrp</a>. In particular, drivers should not use this routine for IRPs created with <a href="kernel.iomakeassociatedirp">IoMakeAssociatedIrp</a>, <a href="kernel.iobuildsynchronousfsdrequest">IoBuildSynchronousFsdRequest</a>, <a href="kernel.iobuildasynchronousfsdrequest">IoBuildAsynchronousFsdRequest</a>, or <a href="kernel.iobuilddeviceiocontrolrequest">IoBuildDeviceIoControlRequest</a>. 

See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561107">Reusing IRPs</a> for more details on how to reuse IRPs. 


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
<dt>Wdm.h (include Ntddk.h)</dt>
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
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_ioreuseirp">IoReuseIrp</a>, <a href="devtest.wdm_ioreuseirp2">IoReuseIrp2</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioinitializeirp">IoInitializeIrp</a>
</dt>
<dt>
<a href="kernel.ioallocateirp">IoAllocateIrp</a>
</dt>
<dt>
<a href="kernel.iomakeassociatedirp">IoMakeAssociatedIrp</a>
</dt>
<dt>
<a href="kernel.irp">IRP</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoReuseIrp routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


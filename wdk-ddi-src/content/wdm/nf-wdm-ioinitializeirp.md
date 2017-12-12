---
UID: NF.wdm.IoInitializeIrp
title: IoInitializeIrp function
author: windows-driver-content
description: The IoInitializeIrp routine initializes a given IRP that was allocated by the caller.
old-location: kernel\ioinitializeirp.htm
old-project: kernel
ms.assetid: 3b5cc1af-ab3b-4583-9ef9-39132789e74f
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: IoInitializeIrp
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
req.alt-api: IoInitializeIrp
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IoReuseIrp, HwStorPortProhibitedDDIs
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

# IoInitializeIrp function



## -description
The <b>IoInitializeIrp</b> routine initializes a given IRP that was allocated by the caller.



## -syntax

````
VOID IoInitializeIrp(
  _Inout_ PIRP   Irp,
  _In_    USHORT PacketSize,
  _In_    CCHAR  StackSize
);
````


## -parameters

### -param Irp [in, out]

Pointer to the IRP to be initialized.


### -param PacketSize [in]

Specifies the size in bytes of the IRP.


### -param StackSize [in]

Specifies the number of stack locations in the IRP. 


## -returns
None


## -remarks
Drivers use <b>IoInitializeIrp</b> to initialize IRPs the driver allocated as raw memory. Do not use <b>IoInitializeIrp</b> to initialize an IRP allocated by <b>IoAllocateIrp</b>. <b>IoAllocateIrp</b> automatically initializes the members of the IRP.

Drivers can use <b>IoInitializeIrp</b> to reinitialize an IRP for reuse only under certain circumstances. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561107">Reusing IRPs</a> for details.

If the driver associates an MDL with the IRP it allocated, the driver is responsible for releasing the MDL when the IRP is completed.

An intermediate or highest-level driver also can call <b>IoBuildDeviceIoControlRequest</b>, <b>IoBuildAsynchronousFsdRequest</b>, or <b>IoBuildSynchronousFsdRequest</b> to set up requests it sends to lower-level drivers. Only a highest-level driver can call <b>IoMakeAssociatedIrp</b>. 


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
<a href="devtest.wdm_ioreuseirp">IoReuseIrp</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioallocateirp">IoAllocateIrp</a>
</dt>
<dt>
<a href="kernel.ioallocatemdl">IoAllocateMdl</a>
</dt>
<dt>
<a href="kernel.iobuildpartialmdl">IoBuildPartialMdl</a>
</dt>
<dt>
<a href="kernel.iofreeirp">IoFreeIrp</a>
</dt>
<dt>
<a href="kernel.iofreemdl">IoFreeMdl</a>
</dt>
<dt>
<a href="kernel.ioreuseirp">IoReuseIrp</a>
</dt>
<dt>
<a href="kernel.iosetnextirpstacklocation">IoSetNextIrpStackLocation</a>
</dt>
<dt>
<a href="kernel.iosizeofirp">IoSizeOfIrp</a>
</dt>
<dt>
<a href="kernel.irp">IRP</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoInitializeIrp routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


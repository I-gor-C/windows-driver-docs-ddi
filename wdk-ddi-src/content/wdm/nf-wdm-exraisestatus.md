---
UID: NF.wdm.ExRaiseStatus
title: ExRaiseStatus function
author: windows-driver-content
description: The ExRaiseStatus routine is called by drivers that supply structured exception handlers to handle particular errors that occur while they are processing I/O requests.
old-location: kernel\exraisestatus.htm
old-project: kernel
ms.assetid: eefbec75-f441-492b-becb-98434253dd62
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: ExRaiseStatus
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
req.alt-api: ExRaiseStatus
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlExPassive, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <=APC_LEVEL
req.product: Windows 10 or later.
---

# ExRaiseStatus function



## -description
The <b>ExRaiseStatus</b> routine is called by drivers that supply structured exception handlers to handle particular errors that occur while they are processing I/O requests.



## -syntax

````
VOID ExRaiseStatus(
  _In_ NTSTATUS Status
);
````


## -parameters

### -param Status [in]

Specifies one of the system-defined STATUS_<i>XXX</i> values. 


## -returns
None


## -remarks
Highest-level drivers, particularly file systems, can call <b>ExRaiseStatus</b>. 


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
&lt;=APC_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqlexpassive">IrqlExPassive</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exraiseaccessviolation">ExRaiseAccessViolation</a>
</dt>
<dt>
<a href="kernel.exraisedatatypemisalignment">ExRaiseDatatypeMisalignment</a>
</dt>
<dt>
<a href="kernel.ioallocateerrorlogentry">IoAllocateErrorLogEntry</a>
</dt>
<dt>
<a href="kernel.kebugcheckex">KeBugCheckEx</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExRaiseStatus routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


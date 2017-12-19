---
UID: NF.ntifs.RtlNtStatusToDosError
title: RtlNtStatusToDosError function
author: windows-driver-content
description: The RtlNtStatusToDosError routine converts the specified NTSTATUS code to its equivalent system error code.
old-location: ifsk\rtlntstatustodoserror.htm
old-project: ifsk
ms.assetid: 9ba6f693-b0b7-4176-b951-7bb259bec391
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RtlNtStatusToDosError
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: The RtlNtStatusToDosError routine is available on Microsoft Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlNtStatusToDosError
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
req.irql: < DISPATCH_LEVEL
---

# RtlNtStatusToDosError function



## -description
The <b>RtlNtStatusToDosError</b> routine converts the specified NTSTATUS code to its equivalent system error code. 



## -syntax

````
ULONG RtlNtStatusToDosError(
  _In_ NTSTATUS Status
);
````


## -parameters

### -param Status [in]

The NTSTATUS code to be converted.


## -returns
<b>RtlNtStatusToDosError</b> returns the corresponding system error code. Error codes are defined in <i>Winerror.h</i>.

<b>RtlNtStatusToDosError</b> returns ERROR_MR_MID_NOT_FOUND when the specified NTSTATUS code does not have a corresponding system error code. For more information about system error codes, see  <a href="base.system_error_codes">System Error Codes</a>. 


## -remarks
There is no function that provides the inverse functionality of <b>RtlNtStatusToDosError</b>, converting a system error code to its corresponding NTSTATUS code. 


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
The RtlNtStatusToDosError routine is available on Microsoft Windows 2000 and later versions of Windows. 

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
&lt; DISPATCH_LEVEL

</td>
</tr>
</table>
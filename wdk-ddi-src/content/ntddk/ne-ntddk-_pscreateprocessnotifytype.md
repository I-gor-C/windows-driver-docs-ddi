---
UID: NE.ntddk._PSCREATEPROCESSNOTIFYTYPE
title: _PSCREATEPROCESSNOTIFYTYPE
author: windows-driver-content
description: Indicates the type of process notification. This enumeration is used in PsSetCreateProcessNotifyRoutineEx2 to register callback notifications.
old-location: kernel\pscreateprocessnotifytype.htm
old-project: kernel
ms.assetid: 5DD02CF1-50E8-45F2-9035-E0AA48F1470C
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _PSCREATEPROCESSNOTIFYTYPE, PSCREATEPROCESSNOTIFYTYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PSCREATEPROCESSNOTIFYTYPE
req.alt-loc: Ntddk.h
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
---

# _PSCREATEPROCESSNOTIFYTYPE enumeration



## -description
Indicates the type of process notification. This enumeration is used in <a href="kernel.pssetcreateprocessnotifyroutineex2">PsSetCreateProcessNotifyRoutineEx2</a> to register callback notifications.



## -syntax

````
typedef enum _PSCREATEPROCESSNOTIFYTYPE { 
  PsCreateProcessNotifySubsystems  = 0
} PSCREATEPROCESSNOTIFYTYPE;
````


## -enum-fields

### -field PsCreateProcessNotifySubsystems

Indicates that the driver-registered callback is invoked for processes of all subsystems, including the Win32 subsystem. Drivers can call <a href="base.ntqueryinformationprocess">NtQueryInformationProcess</a> to determine the underlying subsystem. The query retrieves a  <a href="kernel.subsystem_information_type">SUBSYSTEM_INFORMATION_TYPE</a> value.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10, version 1703

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pssetcreateprocessnotifyroutineex2">PsSetCreateProcessNotifyRoutineEx2</a>
</dt>
<dt>
<a href="kernel.subsystem_information_type">SUBSYSTEM_INFORMATION_TYPE</a>
</dt>
<dt>
<a href="base.ntqueryinformationprocess">NtQueryInformationProcess</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PSCREATEPROCESSNOTIFYTYPE enumeration%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


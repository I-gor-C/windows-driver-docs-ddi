---
UID: NE.ntddk._PSCREATETHREADNOTIFYTYPE
title: PSCREATETHREADNOTIFYTYPE
author: windows-driver-content
description: Indicates the type of thread notification. This enumeration is used in PsSetCreateThreadNotifyRoutineEx to register callback notifications associated with thread creation or deletion.
old-location: kernel\pscreatethreadnotifytype.htm
ms.assetid: C38F8222-7F22-4D6B-A3F2-C326ECE22E8B
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PSCREATETHREADNOTIFYTYPE
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
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
req.iface: 
---

# PSCREATETHREADNOTIFYTYPE enumeration



## -description
<p>Indicates the type of thread notification. This enumeration is used in <a href="https://msdn.microsoft.com/library/windows/hardware/dn957857">PsSetCreateThreadNotifyRoutineEx</a> to register callback notifications associated with thread creation or deletion.</p>


## -syntax

````
typedef enum _PSCREATETHREADNOTIFYTYPE { 
  PsCreateThreadNotifyNonSystem   = 0,
  PsCreateThreadNotifySubsystems  = 1
} PSCREATETHREADNOTIFYTYPE;
````


## -enum-fields
<dl>

### -field <a id="PsCreateThreadNotifyNonSystem"></a><a id="pscreatethreadnotifynonsystem"></a><a id="PSCREATETHREADNOTIFYNONSYSTEM"></a><b>PsCreateThreadNotifyNonSystem</b>

<dd>
<p>The driver-registered callback function is executed on the new non-system thread, which enables the callback function to perform tasks such as setting the initial thread context.
</p>
</dd>

### -field <a id="PsCreateThreadNotifySubsystems"></a><a id="pscreatethreadnotifysubsystems"></a><a id="PSCREATETHREADNOTIFYSUBSYSTEMS"></a><b>PsCreateThreadNotifySubsystems</b>

<dd>
<p>Indicates that the driver-registered callback function is invoked for threads of all subsystems.  Drivers can call <a href="base.ntqueryinformationthread">NtQueryInformationThread</a> to determine the underlying subsystem. The query retrieves a  <a href="https://msdn.microsoft.com/library/windows/hardware/mt805892">SUBSYSTEM_INFORMATION_TYPE</a> value.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957857">PsSetCreateThreadNotifyRoutineEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt805892">SUBSYSTEM_INFORMATION_TYPE</a>
</dt>
<dt>
<a href="base.ntqueryinformationthread">NtQueryInformationThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PSCREATETHREADNOTIFYTYPE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ntifs.RtlSecondsSince1970ToTime
title: RtlSecondsSince1970ToTime function
author: windows-driver-content
description: The RtlSecondsSince1970ToTime routine converts the elapsed time, in seconds, since the beginning of 1970 to an absolute system time value.
old-location: ifsk\rtlsecondssince1970totime.htm
old-project: ifsk
ms.assetid: 8ec961c6-235c-4980-ac4c-60aa496e8a5d
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RtlSecondsSince1970ToTime
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlSecondsSince1970ToTime
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

# RtlSecondsSince1970ToTime function



## -description
The <b>RtlSecondsSince1970ToTime</b> routine converts the elapsed time, in seconds, since the beginning of 1970 to an absolute system time value. 



## -syntax

````
VOID RtlSecondsSince1970ToTime(
  _In_  ULONG          ElapsedSeconds,
  _Out_ PLARGE_INTEGER Time
);
````


## -parameters

### -param ElapsedSeconds [in]

Number of seconds from midnight, December 31, 1969, to the current date and time. 


### -param Time [out]

Pointer to a caller-allocated variable that receives the corresponding current system time. 


## -returns
None


## -remarks
The basis for system time is the start of 1601. The absolute system time is a LARGE_INTEGER value, accurate to 100-nanosecond resolution, assuming an accurate hardware clock. The value returned by <b>RtlSecondsSince1970ToTime</b> is truncated to one-millisecond resolution. 

For more information about converting time values, see <a href="kernel.data_conversions">Data Conversions</a>. 


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

## -see-also
<dl>
<dt>
<a href="ifsk.rtlsecondssince1980totime">RtlSecondsSince1980ToTime</a>
</dt>
<dt>
<a href="kernel.rtltimefieldstotime">RtlTimeFieldsToTime</a>
</dt>
<dt>
<a href="ifsk.rtltimetosecondssince1970">RtlTimeToSecondsSince1970</a>
</dt>
<dt>
<a href="kernel.rtltimetotimefields">RtlTimeToTimeFields</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlSecondsSince1970ToTime routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


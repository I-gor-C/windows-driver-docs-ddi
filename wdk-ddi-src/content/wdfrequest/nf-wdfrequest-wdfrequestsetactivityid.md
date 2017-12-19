---
UID: NF.wdfrequest.WdfRequestSetActivityId
title: WdfRequestSetActivityId function
author: windows-driver-content
description: The WdfRequestSetActivityId method associates an activity identifier with an I/O request.
old-location: wdf\wdfrequestsetactivityid.htm
old-project: wdf
ms.assetid: 05FE0F91-781F-4B8B-87D1-E06BC315856C
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfRequestSetActivityId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WdfRequestSetActivityId
req.alt-loc: WUDFx02000.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WUDFx02000.lib
req.dll: WUDFx02000.dll; TBD
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfRequestSetActivityId function



## -description
<p class="CCE_Message">[Applies to UMDF only]

The <b>WdfRequestSetActivityId</b> method associates an activity identifier with an I/O request.



## -syntax

````
void WdfRequestSetActivityId(
  _In_ WDFREQUEST Request,
  _In_ LPGUID     ActivityId
);
````


## -parameters

### -param Request [in]

A handle to a framework request object.


### -param ActivityId [in]

A pointer to the activity identifier GUID to store in the I/O request.


## -returns
This method does not return a value.


## -remarks
Calling <b>WdfRequestSetActivityId</b> does not set an association with any previously present activity identifier. When the driver calls <b>WdfRequestSetActivityId</b>, any existing activity identifier is overwritten.

To set an association, retrieve the existing identifier by calling <a href="wdf.wdfrequestretrieveactivityid">WdfRequestRetrieveActivityId</a> and then associate the existing identifier with the new one by calling <a href="etw.eventwritetransfer_func">EventWriteTransfer</a>.

The framework does not clear a request's activity identifier when the driver calls <a href="wdf.wdfrequestreuse">WdfRequestReuse</a>.

For more information about activity identifiers, see <a href="wdf.using_activity_identifiers">Using Activity Identifiers</a>.


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
Minimum support

</th>
<td width="70%">
Windows 8.1

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>WUDFx02000.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx02000.dll; </dt>
<dt>TBD</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfrequestretrieveactivityid">WdfRequestRetrieveActivityId</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestSetActivityId method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


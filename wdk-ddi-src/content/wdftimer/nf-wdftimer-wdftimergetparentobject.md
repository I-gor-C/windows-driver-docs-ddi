---
UID: NF.wdftimer.WdfTimerGetParentObject
title: WdfTimerGetParentObject function
author: windows-driver-content
description: The WdfTimerGetParentObject method returns a handle to the parent object of a specified framework timer object.
old-location: wdf\wdftimergetparentobject.htm
old-project: wdf
ms.assetid: 16ac6fea-9eea-4062-8ab9-fd14d80118a6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfTimerGetParentObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdftimer.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfTimerGetParentObject
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfTimerGetParentObject function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WdfTimerGetParentObject</b> method returns a handle to the parent object of a specified framework timer object.


## -syntax

````
WDFOBJECT WdfTimerGetParentObject(
  _In_ WDFTIMER Timer
);
````


## -parameters

### -param Timer [in]

A handle to a framework timer object that was obtained by calling <a href="wdf.wdftimercreate">WdfTimerCreate</a>.

## -returns
<b>WdfTimerGetParentObject</b> returns a handle to the framework object that is the specified timer object's parent object. 

A bug check occurs if the driver supplies an invalid object handle.

## -remarks
For more information about framework timer objects, see <a href="wdf.using_timers">Using Timers</a>.

The following code example shows now an <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function can obtain a timer object's parent. In this example, the driver previously specified that the timer object's parent is a queue object.

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
Minimum KMDF version
</th>
<td width="70%">
1.0
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
<dt>Wdftimer.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdftimercreate">WdfTimerCreate</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfTimerGetParentObject method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

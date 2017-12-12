---
UID: NF.wdftimer.WDF_TIMER_CONFIG_INIT
title: WDF_TIMER_CONFIG_INIT function
author: windows-driver-content
description: The WDF_TIMER_CONFIG_INIT function initializes a WDF_TIMER_CONFIG structure for a timer that will use a single due time.
old-location: wdf\wdf_timer_config_init.htm
old-project: wdf
ms.assetid: 2bf613ff-e178-4a33-a1ae-ea6d4bb78d0a
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WDF_TIMER_CONFIG_INIT
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
req.alt-api: WDF_TIMER_CONFIG_INIT
req.alt-loc: None,None.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: None
req.dll: 
req.irql: Any level
req.product: Windows 10 or later.
---

# WDF_TIMER_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_TIMER_CONFIG_INIT</b> function initializes a <a href="wdf.wdf_timer_config">WDF_TIMER_CONFIG</a> structure for a timer that will use a single due time.



## -syntax

````
VOID WDF_TIMER_CONFIG_INIT(
  _In_ PWDF_TIMER_CONFIG Config,
  _In_ PFN_WDF_TIMER     EvtTimerFunc
);
````


## -parameters

### -param Config [in]

A pointer to a <a href="wdf.wdf_timer_config">WDF_TIMER_CONFIG</a> structure. 


### -param EvtTimerFunc [in]

A pointer to a driver-supplied <a href="wdf.evttimerfunc">EvtTimerFunc</a> callback function. 


## -returns
None


## -remarks
The <b>WDF_TIMER_CONFIG_INIT</b> function zeros the specified <a href="wdf.wdf_timer_config">WDF_TIMER_CONFIG</a> structure. Then it sets the structure's <b>Size</b> member, stores the <i>EvtTimerFunc</i> pointer, sets the <b>Period</b> member and the <b>TolerableDelay</b> member to zero, and sets the <b>AutomaticSerialization</b> member to <b>TRUE</b>. 

For a code example that uses <b>WDF_TIMER_CONFIG_INIT</b>, see <a href="wdf.wdftimercreate">WdfTimerCreate</a>.


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
<dt>None</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evttimerfunc">EvtTimerFunc</a>
</dt>
<dt>
<a href="wdf.wdf_timer_config">WDF_TIMER_CONFIG</a>
</dt>
<dt>
<a href="wdf.wdf_timer_config_init_periodic">WDF_TIMER_CONFIG_INIT_PERIODIC</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_TIMER_CONFIG_INIT function%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


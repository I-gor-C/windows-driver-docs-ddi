---
UID: NF.fwpsk.FwpsvSwitchEventsUnsubscribe0
title: FwpsvSwitchEventsUnsubscribe0
author: windows-driver-content
description: The FwpsvSwitchEventsUnsubscribe0 function releases resources that are associated with virtual switch notification subscriptions.Note  FwpsvSwitchEventsUnsubscribe0 is a specific version of FwpsvSwitchEventsUnsubscribe.
old-location: netvista\fwpsvswitcheventsunsubscribe0.htm
old-project: netvista
ms.assetid: f83c6834-0438-42b8-ad9f-a1d82fcf361c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsvSwitchEventsUnsubscribe0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsvSwitchEventsUnsubscribe0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= PASSIVE_LEVEL
req.iface: 
---

# FwpsvSwitchEventsUnsubscribe0 function



## -description
<p>The <b>FwpsvSwitchEventsUnsubscribe0</b> function releases resources that are associated with virtual switch notification subscriptions.<div class="alert"><b>Note</b>  <b>FwpsvSwitchEventsUnsubscribe0</b> is a specific version of <b>FwpsvSwitchEventsUnsubscribe</b>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>
</p>


## -syntax

````
void NTAPI FwpsvSwitchEventsUnsubscribe0(
   _In_ UINT32            subscriptionId,
   _In_ _Reserved_ UINT32 flags,
   _In_ _Reserved_ void   *reserved
);
````


## -parameters
<dl>

### -param <i>subscriptionId</i> 

<dd>
<p>A unique event subscription identifier that the callout driver obtained by calling  the  <a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a> function.

</p>
</dd>

### -param <i>flags</i> 

<dd>
<p>Reserved. Set this parameter to zero.</p>
</dd>

### -param <i>reserved</i> 

<dd>
<p>Reserved. Set this parameter to  zero.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>
    A callout driver calls the <b>FwpsvSwitchEventsUnsubscribe0</b> function to unsubscribe to virtual switch notifications that the callout driver previously subscribed to  by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a> function. 


   </p>

<p>
    A callout driver calls the <b>FwpsvSwitchEventsUnsubscribe0</b> function to unsubscribe to virtual switch notifications that the callout driver previously subscribed to  by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a> function. 


   </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsvSwitchEventsUnsubscribe0 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

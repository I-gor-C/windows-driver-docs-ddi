---
UID: NF.portcls.IPortClsEtwHelper.MiniportWriteEtwEvent
title: IPortClsEtwHelper::MiniportWriteEtwEvent
author: windows-driver-content
description: The MiniportWriteEtwEvent method is used by an audio miniport driver for providing the information about an Event Tracing for Windows (ETW) event.
old-location: audio\iportclsetwhelper_miniportwriteetwevent.htm
old-project: audio
ms.assetid: 7E0C1140-35AA-424F-8229-21B4F4E1EBDF
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPortClsEtwHelper, MiniportWriteEtwEvent, IPortClsEtwHelper::MiniportWriteEtwEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortClsEtwHelper.MiniportWriteEtwEvent
req.alt-loc: Portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL.
req.iface: IPortClsEtwHelper
---

# IPortClsEtwHelper::MiniportWriteEtwEvent method



## -description
<p>The <code>MiniportWriteEtwEvent</code> method is used by an audio miniport driver for providing the information about an Event Tracing for Windows (ETW) event.</p>


## -syntax

````
NTSTATUS MiniportWriteEtwEvent(
  [in] EPcMiniportEngineEvent miniportEventType,
  [in] ULONGLONG              pvData1,
  [in] ULONGLONG              pvData2,
  [in] ULONGLONG              ulData3,
  [in] ULONGLONG              ulData4
);
````


## -parameters
<dl>

### -param <i>miniportEventType</i> [in]

<dd>
<p>An <a href="..\portcls\ne-portcls-epcminiportengineevent.md">EPcMiniportEngineEvent</a> enumerated value that provides additional error information for reporting glitching errors.</p>
</dd>

### -param <i>pvData1</i> [in]

<dd>
<p>Data parameter.</p>
</dd>

### -param <i>pvData2</i> [in]

<dd>
<p>Data parameter.</p>
</dd>

### -param <i>ulData3</i> [in]

<dd>
<p>Data parameter.</p>
</dd>

### -param <i>ulData4</i> [in]

<dd>
<p>Data parameter.</p>
</dd>
</dl>

## -returns
<p><b>MiniportWriteEtwEvent</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\ne-portcls-epcminiportengineevent.md">EPcMiniportEngineEvent</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iportclsetwhelper.md">IPortClsEtwHelper</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortClsEtwHelper::MiniportWriteEtwEvent method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ks.KsFilterAcquireProcessingMutex
title: KsFilterAcquireProcessingMutex function
author: windows-driver-content
description: The KsFilterAcquireProcessingMutex function acquires the processing mutex for a specified AVStream filter.
old-location: stream\ksfilteracquireprocessingmutex.htm
old-project: stream
ms.assetid: d4a2fe1a-9a16-45b8-b061-9d1b1398e801
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KsFilterAcquireProcessingMutex
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsFilterAcquireProcessingMutex
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
---

# KsFilterAcquireProcessingMutex function



## -description
The<b> KsFilterAcquireProcessingMutex </b>function acquires the processing mutex for a specified AVStream filter. 



## -syntax

````
void KsFilterAcquireProcessingMutex(
  _In_ PKSFILTER Filter
);
````


## -parameters

### -param Filter [in]

A pointer to the <a href="stream.ksfilter">KSFILTER</a> structure representing the AVStream filter for which to acquire the processing mutex.


## -returns
None


## -remarks
AVStream holds the processing control mutex upon return from this routine. For more information, see <a href="https://msdn.microsoft.com/011edaaa-7449-41c3-8cfb-0d319901af8b">Mutexes in AVStream</a>.

A minidriver that must suspend processing for a long period of time should not use this mechanism. Instead, it should manipulate the processing control gate directly by using the <b>KSGATE</b><i>Xxx</i> functions. 


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
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
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
<a href="stream.ksfilterreleaseprocessingmutex">KsFilterReleaseProcessingMutex</a>
</dt>
<dt><b>KsFilterReleaseProcessingMutex</b></dt>
<dt>
<a href="stream.ksfilterattemptprocessing">KsFilterAttemptProcessing</a>
</dt>
<dt>
<a href="stream.kspingetandgate">KsPinGetAndGate</a>
</dt>
<dt>
<a href="stream.kspinacquireprocessingmutex">KsPinAcquireProcessingMutex</a>
</dt>
<dt>
<a href="stream.kspinreleaseprocessingmutex">KsPinReleaseProcessingMutex</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterAcquireProcessingMutex function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


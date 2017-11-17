---
UID: NE.ksmedia.TELEPHONY_PROVIDERCHANGEOP
title: TELEPHONY_PROVIDERCHANGEOP
author: windows-driver-content
description: The TELEPHONY_PROVIDERCHANGEOP enumeration defines constants that specify the requested provider change operation.
old-location: audio\telephony_providerchangeop.htm
ms.assetid: A229E8D5-2776-453B-B0F9-BC48E9D29A2F
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10,Windows 10 Mobile
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TELEPHONY_PROVIDERCHANGEOP
req.alt-loc: ksmedia.h
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
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
req.iface: 
---

# TELEPHONY_PROVIDERCHANGEOP enumeration



## -description
<p>The <b>TELEPHONY_PROVIDERCHANGEOP</b> enumeration defines constants that specify the requested provider change operation.</p>


## -syntax

````
typedef enum  { 
  TELEPHONY_PROVIDERCHANGEOP_END     = 0,
  TELEPHONY_PROVIDERCHANGEOP_BEGIN   = 1,
  TELEPHONY_PROVIDERCHANGEOP_CANCEL  = 2
} TELEPHONY_PROVIDERCHANGEOP;
````


## -enum-fields
<dl>

### -field <a id="TELEPHONY_PROVIDERCHANGEOP_END"></a><a id="telephony_providerchangeop_end"></a><b>TELEPHONY_PROVIDERCHANGEOP_END</b>

<dd>
<p>Specifies that the provider change operation has ended. The audio driver will update the call state to <b>TELEPHONY_CALLSTATE_ENABLED</b> in response to this value.</p>
</dd>

### -field <a id="TELEPHONY_PROVIDERCHANGEOP_BEGIN"></a><a id="telephony_providerchangeop_begin"></a><b>TELEPHONY_PROVIDERCHANGEOP_BEGIN</b>

<dd>
<p>Specifies that the provider change operation has begun. The audio driver will update the call state to <b>TELEPHONY_CALLSTATE_PROVIDERTRANSITION</b> in response to this value.</p>
</dd>

### -field <a id="TELEPHONY_PROVIDERCHANGEOP_CANCEL"></a><a id="telephony_providerchangeop_cancel"></a><b>TELEPHONY_PROVIDERCHANGEOP_CANCEL</b>

<dd>
<p>Specifies that single-radio voice call continuity (SRVCC) is being canceled, and that the audio driver should revert back to the pre-SRVCC state. The audio driver will update the provider call state to TELEPHONY_CALLSTATE_ENABLED in response to this value.</p>
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
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Client</p>
</th>
<td width="70%">
<p>Windows 10 Mobile</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt169876">KSPROPERTY_TELEPHONY_PROVIDERCHANGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt169896">TELEPHONY_CALLSTATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20TELEPHONY_PROVIDERCHANGEOP enumeration%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

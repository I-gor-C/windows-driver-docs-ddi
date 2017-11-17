---
UID: NE.ks.KS_SEEKING_FLAGS
title: KS_SEEKING_FLAGS
author: windows-driver-content
description: The KS_SEEKING_FLAGS enumeration lists positioning options that can be used in conjunction with the KSPROPERTY_POSITIONS structure.
old-location: stream\ks_seeking_flags.htm
ms.assetid: 8e27872e-4f38-4d0e-92bc-5e759a9db195
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_SEEKING_FLAGS
req.alt-loc: ks.h
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
ms.keywords: MIDL_IKeywordDetectorOemAdapter_0003, KEYWORDSELECTOR
req.iface: IKeywordDetectorOemAdapter
---

# KS_SEEKING_FLAGS enumeration



## -description
<p>The KS_SEEKING_FLAGS enumeration lists positioning options that can be used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565207">KSPROPERTY_POSITIONS</a> structure.</p>


## -syntax

````
typedef enum  { 
  KS_SEEKING_NoPositioning           = 0,
  KS_SEEKING_AbsolutePositioning     = 1,
  KS_SEEKING_RelativePositioning     = 2,
  KS_SEEKING_IncrementalPositioning  = 3,
  KS_SEEKING_PositioningBitsMask     = 0x3,
  KS_SEEKING_SeekToKeyFrame          = 0x4,
  KS_SEEKING_ReturnTime              = 0x8
} KS_SEEKING_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="KS_SEEKING_NoPositioning"></a><a id="ks_seeking_nopositioning"></a><a id="KS_SEEKING_NOPOSITIONING"></a><b>KS_SEEKING_NoPositioning</b>

<dd></dd>

### -field <a id="KS_SEEKING_AbsolutePositioning"></a><a id="ks_seeking_absolutepositioning"></a><a id="KS_SEEKING_ABSOLUTEPOSITIONING"></a><b>KS_SEEKING_AbsolutePositioning</b>

<dd></dd>

### -field <a id="KS_SEEKING_RelativePositioning"></a><a id="ks_seeking_relativepositioning"></a><a id="KS_SEEKING_RELATIVEPOSITIONING"></a><b>KS_SEEKING_RelativePositioning</b>

<dd></dd>

### -field <a id="KS_SEEKING_IncrementalPositioning"></a><a id="ks_seeking_incrementalpositioning"></a><a id="KS_SEEKING_INCREMENTALPOSITIONING"></a><b>KS_SEEKING_IncrementalPositioning</b>

<dd></dd>

### -field <a id="KS_SEEKING_PositioningBitsMask"></a><a id="ks_seeking_positioningbitsmask"></a><a id="KS_SEEKING_POSITIONINGBITSMASK"></a><b>KS_SEEKING_PositioningBitsMask</b>

<dd></dd>

### -field <a id="KS_SEEKING_SeekToKeyFrame"></a><a id="ks_seeking_seektokeyframe"></a><a id="KS_SEEKING_SEEKTOKEYFRAME"></a><b>KS_SEEKING_SeekToKeyFrame</b>

<dd></dd>

### -field <a id="KS_SEEKING_ReturnTime"></a><a id="ks_seeking_returntime"></a><a id="KS_SEEKING_RETURNTIME"></a><b>KS_SEEKING_ReturnTime</b>

<dd></dd>
</dl>

## -remarks
<p>The minidriver sets these flag values in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565207">KSPROPERTY_POSITIONS</a> structure that it then submits in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565185">KSPROPERTY_MEDIASEEKING_POSITIONS</a> property request.</p>

<p>The minidriver sets these flag values in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565207">KSPROPERTY_POSITIONS</a> structure that it then submits in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565185">KSPROPERTY_MEDIASEEKING_POSITIONS</a> property request.</p>

<p>The minidriver sets these flag values in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565207">KSPROPERTY_POSITIONS</a> structure that it then submits in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565185">KSPROPERTY_MEDIASEEKING_POSITIONS</a> property request.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565207">KSPROPERTY_POSITIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565185">KSPROPERTY_MEDIASEEKING_POSITIONS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_SEEKING_FLAGS enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.ksmedia._KS_DVDCOPY_BUSKEY
title: KS_DVDCOPY_BUSKEY
author: windows-driver-content
description: The KS_DVDCOPY_BUSKEY structure is used to describe the bus key information for the DVD copyright protection authentication process.
old-location: stream\ks_dvdcopy_buskey.htm
old-project: stream
ms.assetid: bae613e1-c450-4bc0-9370-a7eb8438ae23
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KS_DVDCOPY_BUSKEY, KS_DVDCOPY_BUSKEY, *PKS_DVDCOPY_BUSKEY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_DVDCOPY_BUSKEY
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
req.iface: 
---

# KS_DVDCOPY_BUSKEY structure



## -description
<p>The KS_DVDCOPY_BUSKEY structure is used to describe the bus key information for the DVD copyright protection authentication process.</p>


## -syntax

````
typedef struct _KS_DVDCOPY_BUSKEY {
  BYTE BusKey[5];
  BYTE Reserved[1];
} KS_DVDCOPY_BUSKEY, *PKS_DVDCOPY_BUSKEY;
````


## -struct-fields
<dl>

### -field <b>BusKey</b>

<dd>
<p>Specifies the DVD decoder minidriver's bus key.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>
</dl>

## -remarks
<p>The KS_DVDCOPY_BUSKEY structure is used by both the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565145">KSPROPERTY_DVDCOPY_DVD_KEY1</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff565142">KSPROPERTY_DVDCOPY_DEC_KEY2</a> properties.</p>

<p>For more information, see <a href="NULL">DVD Copyright Protection</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565145">KSPROPERTY_DVDCOPY_DVD_KEY1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565142">KSPROPERTY_DVDCOPY_DEC_KEY2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KS_DVDCOPY_BUSKEY structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.wwan._WWAN_SET_REGISTER_STATE
title: WWAN_SET_REGISTER_STATE
author: windows-driver-content
description: The WWAN_SET_REGISTER_STATE structure represents the command to set the MB device's registration mode and the network provider it should register with.
old-location: netvista\wwan_set_register_state.htm
old-project: netvista
ms.assetid: 617e80c2-2823-4393-81eb-b2cbd2b21be8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WWAN_SET_REGISTER_STATE, WWAN_SET_REGISTER_STATE, *PWWAN_SET_REGISTER_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_SET_REGISTER_STATE
req.alt-loc: wwan.h
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
req.product: Windows 10 or later.
---

# WWAN_SET_REGISTER_STATE structure



## -description
<p>The WWAN_SET_REGISTER_STATE structure represents the command to set the MB device's registration mode
  and the network provider it should register with.</p>


## -syntax

````
typedef struct _WWAN_SET_REGISTER_STATE {
  WCHAR                ProviderId[WWAN_PROVIDERID_LEN];
  WWAN_REGISTER_ACTION RegisterAction;
  ULONG                WwanDataClass;
} WWAN_SET_REGISTER_STATE, *PWWAN_SET_REGISTER_STATE;
````


## -struct-fields
<dl>

### -field <b>ProviderId</b>

<dd>
<p>A NULL-terminated numeric (0-9) string that represents the network provider identity.
     </p>
<p>For GSM-based networks, this string is a concatenation of a three-digit Mobile Country Code (MCC) and
     a two or three-digit Mobile Network Code (MNC). GSM-based carriers may have more than one MNC, and hence
     more than one 
     <b>ProviderId</b> .</p>
<p>For CDMA-based networks, this string is a five-digit System ID (SID). Generally, a CDMA-based carrier
     has more than one SID. Typically, the carrier has one SID for each market, which is usually divided
     geographically within a nation by regulations, such as Metropolitan Statistical Areas (MSA) in the
     United States of America. Miniport drivers of CDMA-based devices must specify
     WWAN_CDMA_DEFAULT_PROVIDER_ID if this information is not available.</p>
</dd>

### -field <b>RegisterAction</b>

<dd>
<p>The registration action that the miniport driver is requested to perform. If this member is set to
     
     <b>WwanRegisterActionAutomatic</b>, the 
     <b>ProviderId</b> member should be ignored.</p>
</dd>

### -field <b>WwanDataClass</b>

<dd>
<p>A bitmap that represents the data access technologies that are preferred for a connection. For a
     detailed list of values, see the 
     <b>WwanDataClass</b> member of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571204">WWAN_DEVICE_CAPS</a>.
     </p>
<p>When multiple data-classes are set as preferred, miniport drivers are expected register to the
     highest available data-class technology that is currently visible. Miniport drivers should attempt to
     register the best available data-class as requested. If the device cannot register the data-class
     specified in this member, it should register the best available data-class.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571228">WWAN_REGISTER_ACTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567926">NDIS_WWAN_SET_REGISTER_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SET_REGISTER_STATE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

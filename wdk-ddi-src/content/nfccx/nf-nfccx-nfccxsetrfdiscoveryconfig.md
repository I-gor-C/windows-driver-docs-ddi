---
UID: NF.nfccx.NfcCxSetRfDiscoveryConfig
title: NfcCxSetRfDiscoveryConfig function
author: windows-driver-content
description: Called by the client driver to configure the RF discovery parameters.
old-location: nfpdrivers\_nfccxsetrfdiscoveryconfig.htm
old-project: nfpdrivers
ms.assetid: D0190BA1-196D-4F8B-A367-80272F094B6B
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NfcCxSetRfDiscoveryConfig
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: nfccx.h
req.include-header: Ncidef.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NfcCxSetRfDiscoveryConfig
req.alt-loc: NfcCx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Nfccxstub.lib
req.dll: NfcCx.dll
req.irql: 
---

# NfcCxSetRfDiscoveryConfig function



## -description
Called by the client driver to configure the RF discovery parameters.



## -syntax

````
NTSTATUS NfcCxSetRfDiscoveryConfig(
   WDFDEVICE                    Device,
   PCNFC_CX_RF_DISCOVERY_CONFIG Config
);
````


## -parameters

### -param Device 

A handle to a framework device object.


### -param Config 

A pointer to an <a href="nfpdrivers.nfc_cx_rf_discovery_config">NFC_CX_RF_DISCOVERY_CONFIG</a> structure.


## -returns
If the operation succeeds, the function returns STATUS_SUCCESS.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
None supported

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Nfccx.h (include Ncidef.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Nfccxstub.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NfcCx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?LinkID=785320">Near field communication (NFC) design guide</a></dt>
<dt><a href="https://msdn.microsoft.com/windows/hardware/drivers/nfc/nfc-class-extension-">NFC class extension design guide</a></dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [nfpdrivers\nfpdrivers]:%20NfcCxSetRfDiscoveryConfig method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


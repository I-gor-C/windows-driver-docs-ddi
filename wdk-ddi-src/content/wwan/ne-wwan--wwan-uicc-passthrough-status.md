---
UID: NE.wwan._WWAN_UICC_PASSTHROUGH_STATUS
title: WWAN_UICC_PASSTHROUGH_STATUS
author: windows-driver-content
description: The WWAN_UICC_PASSTHROUGH_STATUS enumeration defines the passthrough status of a modem miniport adapter for a UICC smart card.
old-location: netvista\wwan_uicc_passthrough_status.htm
old-project: netvista
ms.assetid: 93D35A64-8394-41C2-BFB8-C8DE93619E75
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_UICC_PASSTHROUGH_STATUS
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

# WWAN_UICC_PASSTHROUGH_STATUS enumeration



## -description
<p>The <b>WWAN_UICC_PASSTHROUGH_STATUS</b> enumeration defines the passthrough status of a modem miniport adapter for a UICC smart card.</p>


## -syntax

````
typedef enum _WWAN_UICC_PASSTHROUGH_STATUS { 
  WwanUiccPassThroughDisabled  = 0,
  WwanUiccPassThroughEnabled   = 1,
  WwanUiccPassThroughMaximum
} WWAN_UICC_PASSTHROUGH_STATUS;
````


## -enum-fields
<dl>

### -field <a id="WwanUiccPassThroughDisabled"></a><a id="wwanuiccpassthroughdisabled"></a><a id="WWANUICCPASSTHROUGHDISABLED"></a><b>WwanUiccPassThroughDisabled</b>

<dd>
<p>Indicates that passthrough to the UICC is disabled. When UICC passthrough is disabled, the MB host treats the UICC as a regular Telecom UICC and expects a Telecom UICC file system to be present on the UICC.</p>
</dd>

### -field <a id="WwanUiccPassThroughEnabled"></a><a id="wwanuiccpassthroughenabled"></a><a id="WWANUICCPASSTHROUGHENABLED"></a><b>WwanUiccPassThroughEnabled</b>

<dd>
<p>Indicates that passthrough to the UICC is enabled. When UICC passthrough is enabled, the modem miniport adapter treats the UICC as if it were in a passthrough mode that enables communication between the host and UICC, even if the UICC has no Telecom UICC file system. The miniport adapter does not send any APDUs to the card and does not interfere at any time with the communication between the host and the UICC.</p>
</dd>

### -field <a id="WwanUiccPassThroughMaximum"></a><a id="wwanuiccpassthroughmaximum"></a><a id="WWANUICCPASSTHROUGHMAXIMUM"></a><b>WwanUiccPassThroughMaximum</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</p>
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
<p>Windows 10, version 1709</p>
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
<a href="..\wwan\ns-wwan--wwan-uicc-reset-info.md">WWAN_UICC_RESET_INFO</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-uicc-reset-operations">MB UICC reset operations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_UICC_PASSTHROUGH_STATUS enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

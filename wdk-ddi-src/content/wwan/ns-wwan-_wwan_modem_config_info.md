---
UID: NS:wwan._WWAN_MODEM_CONFIG_INFO
title: _WWAN_MODEM_CONFIG_INFO
author: windows-driver-content
description: The WWAN_MODEM_CONFIG_INFO structure represents the modem's configuration information.
old-location: netvista\wwan_modem_config_info.htm
old-project: netvista
ms.assetid: 14FBFA51-F4A5-417A-8905-241CEA543774
ms.author: windowsdriverdev
ms.date: 1/8/2018
ms.keywords: _WWAN_MODEM_CONFIG_INFO, WWAN_MODEM_CONFIG_INFO, *PWWAN_MODEM_CONFIG_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_MODEM_CONFIG_INFO
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
req.typenames: WWAN_MODEM_CONFIG_INFO, *PWWAN_MODEM_CONFIG_INFO
req.product: Windows 10 or later.
---

# _WWAN_MODEM_CONFIG_INFO structure



## -description
The <b>WWAN_MODEM_CONFIG_INFO</b> structure represents the modem's configuration information.



## -syntax

````
typedef struct _WWAN_MODEM_CONFIG_INFO {
  WWAN_MODEM_CONFIG_STATUS ConfigStatus;
  WWAN_MODEM_CONFIG_MODE   ConfigMode;
} WWAN_MODEM_CONFIG_INFO, *PWWAN_MODEM_CONFIG_INFO;
````


## -struct-fields

### -field ConfigStatus

A formatted <a href="..\wwan\ns-wwan-_wwan_modem_config_status.md">WWAN_MODEM_CONFIG_STATUS</a> structure containing the modem's configuration (config) status.


### -field ConfigMode

The modem's configuration mode. For a list of defined values, see <a href="..\wwan\ne-wwan-_wwan_modem_config_mode.md">WWAN_MODEM_CONFIG_MODE</a>.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Windows 10, version 1709

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="..\wwan\ns-wwan-_wwan_modem_config_status.md">WWAN_MODEM_CONFIG_STATUS</a>
</dt>
<dt>
<a href="..\wwan\ne-wwan-_wwan_modem_config_mode.md">WWAN_MODEM_CONFIG_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9D56BCE1-2CCF-4BD0-A646-4510642EB08A">NDIS_STATUS_WWAN_MODEM_CONFIG_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/527B970C-09FC-4E49-A309-44D5C6A39778">OID_WWAN_MODEM_CONFIG_INFO</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan-_ndis_wwan_modem_config_info.md">NDIS_WWAN_MODEM_CONFIG_INFO</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_MODEM_CONFIG_INFO structure%20 RELEASE:%20(1/8/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


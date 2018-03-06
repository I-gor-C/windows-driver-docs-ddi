---
UID: NE:wwan._WWAN_MODEM_CONFIG_REASON
title: "_WWAN_MODEM_CONFIG_REASON"
author: windows-driver-content
description: The WWAN_MODEM_CONFIG_REASON enumeration lists definitions for reasons why a modem's configuration state change was triggered.
old-location: netvista\wwan_modem_config_reason.htm
old-project: netvista
ms.assetid: 2CF2C69B-A5DF-4A78-BC15-EB80FAC51831
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PWWAN_MODEM_CONFIG_REASON, PWWAN_MODEM_CONFIG_REASON, PWWAN_MODEM_CONFIG_REASON enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_MODEM_CONFIG_REASON, WWAN_MODEM_CONFIG_REASON enumeration [Network Drivers Starting with Windows Vista], WwanModemConfigReasonActivationFailure, WwanModemConfigReasonConfigFileUpdate, WwanModemConfigReasonIMSIReset, WwanModemConfigReasonMax, WwanModemConfigReasonModemRecovery, WwanModemConfigReasonModemReset, WwanModemConfigReasonNOSIM, WwanModemConfigReasonNone, WwanModemConfigReasonSIMDetected, WwanModemConfigReasonSIMRemoved, _WWAN_MODEM_CONFIG_REASON, netvista.wwan_modem_config_reason, wwan/PWWAN_MODEM_CONFIG_REASON, wwan/WWAN_MODEM_CONFIG_REASON, wwan/WwanModemConfigReasonActivationFailure, wwan/WwanModemConfigReasonConfigFileUpdate, wwan/WwanModemConfigReasonIMSIReset, wwan/WwanModemConfigReasonMax, wwan/WwanModemConfigReasonModemRecovery, wwan/WwanModemConfigReasonModemReset, wwan/WwanModemConfigReasonNOSIM, wwan/WwanModemConfigReasonNone, wwan/WwanModemConfigReasonSIMDetected, wwan/WwanModemConfigReasonSIMRemoved"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wwan.h
api_name:
-	WWAN_MODEM_CONFIG_REASON
product: Windows
targetos: Windows
req.typenames: WWAN_MODEM_CONFIG_REASON, *PWWAN_MODEM_CONFIG_REASON
req.product: Windows 10 or later.
---

# _WWAN_MODEM_CONFIG_REASON Enumeration
The <b>WWAN_MODEM_CONFIG_REASON</b> enumeration lists definitions for reasons why a modem's configuration state change was triggered.

## Syntax
````
typedef enum _WWAN_MODEM_CONFIG_REASON { 
  WwanModemConfigReasonNone               = 0,
  WwanModemConfigReasonSIMDetected,
  WwanModemConfigReasonSIMRemoved,
  WwanModemConfigReasonNOSIM,
  WwanModemConfigReasonIMSIReset,
  WwanModemConfigReasonActivationFailure,
  WwanModemConfigReasonConfigFileUpdate,
  WwanModemConfigReasonModemReset,
  WwanModemConfigReasonModemRecovery,
  WwanModemConfigReasonMax
} WWAN_MODEM_CONFIG_REASON, *PWWAN_MODEM_CONFIG_REASON;
````

## Constants

<table>
            
                <tr>
                    <td>WwanModemConfigReasonActivationFailure</td>
                    <td>Optional. Activation of a new configuration failed.</td>
                </tr>
            
                <tr>
                    <td>WwanModemConfigReasonConfigFileUpdate</td>
                    <td>Optional. A new configuration file was updated by the host.</td>
                </tr>
            
                <tr>
                    <td>WwanModemConfigReasonIMSIReset</td>
                    <td>Optional. A SIM card was reset with new IMSI programmed into it.</td>
                </tr>
            
                <tr>
                    <td>WwanModemConfigReasonMax</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
                </tr>
            
                <tr>
                    <td>WwanModemConfigReasonModemRecovery</td>
                    <td>Required. The modem reset and configuration was restored to default.</td>
                </tr>
            
                <tr>
                    <td>WwanModemConfigReasonModemReset</td>
                    <td>Optional. The modem reset and configuration was not lost.</td>
                </tr>
            
                <tr>
                    <td>WwanModemConfigReasonNone</td>
                    <td>Default value that can be used if other optional reasons are not supported.</td>
                </tr>
            
                <tr>
                    <td>WwanModemConfigReasonNOSIM</td>
                    <td>Optional. There is no SIM card.</td>
                </tr>
            
                <tr>
                    <td>WwanModemConfigReasonSIMDetected</td>
                    <td>Required. A SIM card was detected by a modem.</td>
                </tr>
            
                <tr>
                    <td>WwanModemConfigReasonSIMRemoved</td>
                    <td>Optional. A SIM card was removed.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows 10, version 1709 |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="..\wwan\ns-wwan-_wwan_modem_config_status.md">WWAN_MODEM_CONFIG_STATUS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_MODEM_CONFIG_REASON enumeration%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
---
UID : NS:windot11.DOT11_HRDSSS_PHY_ATTRIBUTES
title : DOT11_HRDSSS_PHY_ATTRIBUTES
author : windows-driver-content
description : Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location : netvista\dot11_hrdsss_phy_attributes.htm
old-project : netvista
ms.assetid : 435e74b4-1a29-4031-bf21-92eae71e99a1
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : DOT11_HRDSSS_PHY_ATTRIBUTES, DOT11_HRDSSS_PHY_ATTRIBUTES, *PDOT11_HRDSSS_PHY_ATTRIBUTES
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : windot11.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DOT11_HRDSSS_PHY_ATTRIBUTES
req.alt-loc : windot11.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : DOT11_HRDSSS_PHY_ATTRIBUTES, *PDOT11_HRDSSS_PHY_ATTRIBUTES
req.product : Windows 10 or later.
---

# DOT11_HRDSSS_PHY_ATTRIBUTES structure


## Syntax
````
typedef struct DOT11_HRDSSS_PHY_ATTRIBUTES {
  BOOLEAN bShortPreambleOptionImplemented;
  BOOLEAN bPBCCOptionImplemented;
  BOOLEAN bChannelAgilityPresent;
  ULONG   uHRCCAModeSupported;
} DOT11_HRDSSS_PHY_ATTRIBUTES, *PDOT11_HRDSSS_PHY_ATTRIBUTES;
````

## Members

        
            `bChannelAgilityPresent`

            A Boolean value that, if set to <b>TRUE</b>, specifies that the PHY supports channel agility. For more
     information about channel agility, refer to Clause 18 of the IEEE 802.11b-1999 standard and Clause 19 of
     the IEEE 802.11g-2003 standard.
        
            `bPBCCOptionImplemented`

            A Boolean value that, if set to <b>TRUE</b>, specifies that the PHY supports enabled packet binary
     convolutional code (PBCC) modulation. For more information about PBCC modulation, refer to Clause
     18.4.6.6 of the IEEE 802.11b-1999 standard.
        
            `bShortPreambleOptionImplemented`

            A Boolean value that, if set to <b>TRUE</b>, specifies that the PHY supports the option to enable the
     short Physical Layer Convergence Procedure (PLCP) preamble and header. For more information about the
     short PLCP preamble and header, refer to Clause 18.2.2.2 of the IEEE 802.11b-1999 standard
        
            `uHRCCAModeSupported`

            The type of clear channel assessment (CCA) mode supported by the current PHY type. For more
     information about CCA, refer to Clause 16.4.8.5 of the IEEE 802.11-2012 standard and Clause 18.4.8.4 of
     the IEEE 802.11b-1999 standard.
     

The CCA modes supported by the PHY are defined through the following bitmask:

    ## Remarks
        The miniport driver defines the attributes of a PHY on the 802.11 station through the 
    <a href="..\windot11\ns-windot11-dot11_phy_attributes.md">DOT11_PHY_ATTRIBUTES</a> structure, and
    formats the 
    <b>HRDSSSAttributes</b> member as a DOT11_HRDSSS_PHY_ATTRIBUTES structure. The driver must only do this if
    the PHY defined by the DOT11_PHY_ATTRIBUTES structure is an HRDSSS PHY type.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | windot11.h (include Ndis.h) |

    ## See Also

        <dl>
<dt>
<a href="..\windot11\ns-windot11-dot11_phy_attributes.md">DOT11_PHY_ATTRIBUTES</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_HRDSSS_PHY_ATTRIBUTES structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
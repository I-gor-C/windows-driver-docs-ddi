---
UID : NS:windot11.DOT11_VWIFI_ATTRIBUTES
title : DOT11_VWIFI_ATTRIBUTES
author : windows-driver-content
description : Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location : netvista\dot11_vwifi_attributes.htm
old-project : netvista
ms.assetid : 46eee6ea-8259-4036-b1c4-f0eef6587879
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : DOT11_VWIFI_ATTRIBUTES, *PDOT11_VWIFI_ATTRIBUTES, DOT11_VWIFI_ATTRIBUTES
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : windot11.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 7 and later versions of the Windows operating   system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DOT11_VWIFI_ATTRIBUTES
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
req.typenames : "*PDOT11_VWIFI_ATTRIBUTES, DOT11_VWIFI_ATTRIBUTES"
req.product : Windows 10 or later.
---

# DOT11_VWIFI_ATTRIBUTES structure


## Syntax
````
typedef struct DOT11_VWIFI_ATTRIBUTES {
  NDIS_OBJECT_HEADER      Header;
  ULONG                   uTotalNumOfEntries;
  DOT11_VWIFI_COMBINATION Combinations[1];
} DOT11_VWIFI_ATTRIBUTES, *PDOT11_VWIFI_ATTRIBUTES;
````

## Members

        
            `Header`

            The type, revision, and size of the DOT11_VWIFI_ATTRIBUTES structure. This member is formatted as
     an 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure.
     

The miniport driver must set the members of 
     <b>Header</b> to the following values:
        
            `uTotalNumOfEntries`

            The maximum number of entries that the 
     <b>Combinations</b> array can contain.


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
<a href="..\windot11\ns-windot11-_dot11_vwifi_combination.md">DOT11_VWIFI_COMBINATION</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11-_dot11_vwifi_combination_v2.md">DOT11_VWIFI_COMBINATION_V2</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_VWIFI_ATTRIBUTES structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
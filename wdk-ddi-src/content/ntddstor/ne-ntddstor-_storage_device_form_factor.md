---
UID: NE:ntddstor._STORAGE_DEVICE_FORM_FACTOR
title: "_STORAGE_DEVICE_FORM_FACTOR"
author: windows-driver-content
description: Indicates the form factor of a storage device.
old-location: storage\storage_device_form_factor.htm
old-project: storage
ms.assetid: EE59767B-2504-4E5F-A442-60EEBEE70B59
ms.author: windowsdriverdev
ms.date: 1/10/2018
ms.keywords: FormFactor1_8Less, ntddstor/FormFactorPCIeBoard, *PSTORAGE_DEVICE_FORM_FACTOR, ntddstor/FormFactor1_8, FormFactor2_5, ntddstor/FormFactor2_5, FormFactorM_2, FormFactorMemoryCard, STORAGE_DEVICE_FORM_FACTOR, ntddstor/FormFactorEmbedded, ntddstor/FormFactorDimm, PSTORAGE_DEVICE_FORM_FACTOR, ntddstor/PSTORAGE_DEVICE_FORM_FACTOR, ntddstor/FormFactorM_2, FormFactorUnknown, STORAGE_DEVICE_FORM_FACTOR enumeration [Storage Devices], ntddstor/FormFactor3_5, storage.storage_device_form_factor, FormFactor3_5, ntddstor/FormFactor1_8Less, _STORAGE_DEVICE_FORM_FACTOR, FormFactorDimm, FormFactorEmbedded, FormFactormSata, FormFactorPCIeBoard, ntddstor/STORAGE_DEVICE_FORM_FACTOR, ntddstor/FormFactorMemoryCard, PSTORAGE_DEVICE_FORM_FACTOR enumeration pointer [Storage Devices], ntddstor/FormFactormSata, FormFactor1_8, ntddstor/FormFactorUnknown
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Ntddstor.h
apiname:
-	STORAGE_DEVICE_FORM_FACTOR
product: Windows
targetos: Windows
req.typenames: "*PSTORAGE_DEVICE_FORM_FACTOR, STORAGE_DEVICE_FORM_FACTOR"
---

# _STORAGE_DEVICE_FORM_FACTOR Enumeration
Indicates the form factor of a storage device.

## Syntax
````
typedef enum _STORAGE_DEVICE_FORM_FACTOR { 
  FormFactorUnknown     = 0, // 0x0
  FormFactor3_5,
  FormFactor2_5,
  FormFactor1_8,
  FormFactor1_8Less,
  FormFactorEmbedded,
  FormFactorMemoryCard,
  FormFactormSata,
  FormFactorM_2,
  FormFactorPCIeBoard,
  FormFactorDimm
} STORAGE_DEVICE_FORM_FACTOR, *PSTORAGE_DEVICE_FORM_FACTOR;
````

## Constants

<table>
            
                <tr>
                    <td>FormFactor1_8</td>
                    <td>1.8 inch nominal form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactor1_8Less</td>
                    <td>Less than 1.8 inch nominal form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactor2_5</td>
                    <td>2.5 inch nominal form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactor3_5</td>
                    <td>3.5 inch nominal form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactorDimm</td>
                    <td>Dual in-line memory module (DIMM) slot form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactorEmbedded</td>
                    <td>The storage device is embedded on a board.</td>
                </tr>
            
                <tr>
                    <td>FormFactorM_2</td>
                    <td>M.2 form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactorMemoryCard</td>
                    <td>A memory card, such as SmartMedia or CompactFlash.</td>
                </tr>
            
                <tr>
                    <td>FormFactormSata</td>
                    <td>Mini-SATA (mSATA) form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactorPCIeBoard</td>
                    <td>PCI Express (PCIe) card form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactorUnknown</td>
                    <td>Unknown form factor.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddstor.h (include Ntddstor.h) |
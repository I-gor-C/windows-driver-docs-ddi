---
UID: NE:ntddmmc._FEATURE_PROFILE_TYPE
title: "_FEATURE_PROFILE_TYPE"
author: windows-driver-content
description: The FEATURE_PROFILE_TYPE enumeration provides a list of the profile names that are defined by the SCSI Multimedia - 4 (MMC-4) specification.
old-location: storage\feature_profile_type.htm
old-project: storage
ms.assetid: 60cce78f-1025-41a7-861d-150ef28376cb
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PFEATURE_PROFILE_TYPE, FEATURE_PROFILE_TYPE, FEATURE_PROFILE_TYPE enumeration [Storage Devices], PFEATURE_PROFILE_TYPE, PFEATURE_PROFILE_TYPE enumeration pointer [Storage Devices], ProfileAS_MO, ProfileBDRRandomWritable, ProfileBDRSequentialWritable, ProfileBDRewritable, ProfileBDRom, ProfileCdRecordable, ProfileCdRewritable, ProfileCdrom, ProfileDDCdRecordable, ProfileDDCdRewritable, ProfileDDCdrom, ProfileDvdDashRDualLayer, ProfileDvdDashRLayerJump, ProfileDvdPlusR, ProfileDvdPlusRDualLayer, ProfileDvdPlusRW, ProfileDvdPlusRWDualLayer, ProfileDvdRWSequential, ProfileDvdRam, ProfileDvdRecordable, ProfileDvdRewritable, ProfileDvdRom, ProfileHDDVDRDualLayer, ProfileHDDVDRWDualLayer, ProfileHDDVDRam, ProfileHDDVDRecordable, ProfileHDDVDRewritable, ProfileHDDVDRom, ProfileInvalid, ProfileMOErasable, ProfileMOWriteOnce, ProfileNonRemovableDisk, ProfileNonStandard, ProfileRemovableDisk, _FEATURE_PROFILE_TYPE, ntddmmc/FEATURE_PROFILE_TYPE, ntddmmc/PFEATURE_PROFILE_TYPE, ntddmmc/ProfileAS_MO, ntddmmc/ProfileBDRRandomWritable, ntddmmc/ProfileBDRSequentialWritable, ntddmmc/ProfileBDRewritable, ntddmmc/ProfileBDRom, ntddmmc/ProfileCdRecordable, ntddmmc/ProfileCdRewritable, ntddmmc/ProfileCdrom, ntddmmc/ProfileDDCdRecordable, ntddmmc/ProfileDDCdRewritable, ntddmmc/ProfileDDCdrom, ntddmmc/ProfileDvdDashRDualLayer, ntddmmc/ProfileDvdDashRLayerJump, ntddmmc/ProfileDvdPlusR, ntddmmc/ProfileDvdPlusRDualLayer, ntddmmc/ProfileDvdPlusRW, ntddmmc/ProfileDvdPlusRWDualLayer, ntddmmc/ProfileDvdRWSequential, ntddmmc/ProfileDvdRam, ntddmmc/ProfileDvdRecordable, ntddmmc/ProfileDvdRewritable, ntddmmc/ProfileDvdRom, ntddmmc/ProfileHDDVDRDualLayer, ntddmmc/ProfileHDDVDRWDualLayer, ntddmmc/ProfileHDDVDRam, ntddmmc/ProfileHDDVDRecordable, ntddmmc/ProfileHDDVDRewritable, ntddmmc/ProfileHDDVDRom, ntddmmc/ProfileInvalid, ntddmmc/ProfileMOErasable, ntddmmc/ProfileMOWriteOnce, ntddmmc/ProfileNonRemovableDisk, ntddmmc/ProfileNonStandard, ntddmmc/ProfileRemovableDisk, storage.feature_profile_type, structs-CD-ROM_89bf20da-a096-4f37-ab24-219533578d34.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddmmc.h
req.include-header: Ntddcdrm.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddmmc.h
api_name:
-	FEATURE_PROFILE_TYPE
product: Windows
targetos: Windows
req.typenames: FEATURE_PROFILE_TYPE, *PFEATURE_PROFILE_TYPE
---

# _FEATURE_PROFILE_TYPE Enumeration
The FEATURE_PROFILE_TYPE enumeration provides a list of the profile names that are defined by the <i>SCSI Multimedia - 4 (MMC-4)</i> specification.

## Syntax
```
typedef enum _FEATURE_PROFILE_TYPE {
  ProfileInvalid                ,
  ProfileNonRemovableDisk       ,
  ProfileRemovableDisk          ,
  ProfileMOErasable             ,
  ProfileMOWriteOnce            ,
  ProfileAS_MO                  ,
  ProfileCdrom                  ,
  ProfileCdRecordable           ,
  ProfileCdRewritable           ,
  ProfileDvdRom                 ,
  ProfileDvdRecordable          ,
  ProfileDvdRam                 ,
  ProfileDvdRewritable          ,
  ProfileDvdRWSequential        ,
  ProfileDvdDashRDualLayer      ,
  ProfileDvdDashRLayerJump      ,
  ProfileDvdPlusRW              ,
  ProfileDvdPlusR               ,
  ProfileDDCdrom                ,
  ProfileDDCdRecordable         ,
  ProfileDDCdRewritable         ,
  ProfileDvdPlusRWDualLayer     ,
  ProfileDvdPlusRDualLayer      ,
  ProfileBDRom                  ,
  ProfileBDRSequentialWritable  ,
  ProfileBDRRandomWritable      ,
  ProfileBDRewritable           ,
  ProfileHDDVDRom               ,
  ProfileHDDVDRecordable        ,
  ProfileHDDVDRam               ,
  ProfileHDDVDRewritable        ,
  ProfileHDDVDRDualLayer        ,
  ProfileHDDVDRWDualLayer       ,
  ProfileNonStandard
} *PFEATURE_PROFILE_TYPE, FEATURE_PROFILE_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>ProfileInvalid</td>
                    <td>Does not indicate a valid profile.</td>
                </tr>
            
                <tr>
                    <td>ProfileNonRemovableDisk</td>
                    <td>Indicates the profile named "Nonremovable disk" by the <i>SCSI-3 Multimedia (MMC-3)</i> specification. This profile is used with devices that manage rewritable media and are capable of changing behavior.</td>
                </tr>
            
                <tr>
                    <td>ProfileRemovableDisk</td>
                    <td>Indicates the profile named "Removable disk" by the <i>MMC-3</i> specification. This profile is used with devices that manage rewritable, removable media.</td>
                </tr>
            
                <tr>
                    <td>ProfileMOErasable</td>
                    <td>Indicates the profile named "MO Erasable" by the <i>MMC-3</i> specification. This profile is used with devices that manage magneto-optical media and that have a sector-erase capability.</td>
                </tr>
            
                <tr>
                    <td>ProfileMOWriteOnce</td>
                    <td>Indicates the profile named "MO Write Once" by the <i>MMC-3</i> specification. This profile is used with devices that manage magneto-optical write-once media.</td>
                </tr>
            
                <tr>
                    <td>ProfileAS_MO</td>
                    <td>Indicates the profile named "AS-MO" by the <i>MMC-3</i> specification. This profile is used with devices that implement Advance Storage technology and manage magneto-optical media.</td>
                </tr>
            
                <tr>
                    <td>ProfileCdrom</td>
                    <td>Indicates the profile named "CD-ROM" by the <i>MMC-3</i> specification. This profile is used with devices that manage read-only compact disc media.</td>
                </tr>
            
                <tr>
                    <td>ProfileCdRecordable</td>
                    <td>Indicates the profile named "CD-R" by the <i>MMC-3</i> specification. This profile is used with devices that manage write-once compact disc media.</td>
                </tr>
            
                <tr>
                    <td>ProfileCdRewritable</td>
                    <td>Indicates the profile named "CD-RW" by the <i>MMC-3</i> specification. This profile is used with devices that manage rewritable compact disc media.</td>
                </tr>
            
                <tr>
                    <td>ProfileDvdRom</td>
                    <td>Indicates the profile named "DVD-ROM" by the <i>MMC-3</i> specification. This profile is used with devices that manage read-only DVD media.</td>
                </tr>
            
                <tr>
                    <td>ProfileDvdRecordable</td>
                    <td>Indicates the profile named "DVD-R" by the <i>MMC-3</i> specification. This profile is used with devices that manage write-once DVD media and operate in sequential recording mode.</td>
                </tr>
            
                <tr>
                    <td>ProfileDvdRam</td>
                    <td>Indicates the profile named "DVD-RAM or DVD+RW" by the <i>MMC-3</i> specification. This profile is used with devices that manage rewritable DVD media.</td>
                </tr>
            
                <tr>
                    <td>ProfileDvdRewritable</td>
                    <td>Indicates the profile named "DVD-RW Restricted Overwrite" by the <i>MMC-3</i> specification. This profile is used with devices that manage rerecordable DVD media and operate in packet-writing mode.</td>
                </tr>
            
                <tr>
                    <td>ProfileDvdRWSequential</td>
                    <td>Indicates the profile named "DVD-RW Sequential Recording" by the <i>MMC-3</i> specification. This profile is used with devices that implement a series of features associated with sequential recording, such as the features "Incremental Streaming Writable" and "Real-Time Streaming". For a full list of the features supported with this profile, see the <i>MMC-3</i> specification.</td>
                </tr>
            
                <tr>
                    <td>ProfileDvdDashRDualLayer</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ProfileDvdDashRLayerJump</td>
                    <td>Reserved 0x0017 - 0x0019</td>
                </tr>
            
                <tr>
                    <td>ProfileDvdPlusRW</td>
                    <td>Indicates the profile named "DVD+RW" by the <i>MMC-3</i> specification. This profile is used with devices that implement a series of features required to manage DVD media that is both readable and writable. For a full list of the features supported with this profile, see the <i>MMC-3</i> specification.</td>
                </tr>
            
                <tr>
                    <td>ProfileDvdPlusR</td>
                    <td>Reserved 0x001C - 001F</td>
                </tr>
            
                <tr>
                    <td>ProfileDDCdrom</td>
                    <td>Indicates the profile named "DDCD-ROM" by the <i>MMC-3</i> specification. This profile is used with devices that can read "DDCD specific structure." For a full list of the features supported with this profile, see the <i>MMC-3</i> specification.</td>
                </tr>
            
                <tr>
                    <td>ProfileDDCdRecordable</td>
                    <td>Indicates the profile named "DDCD-R" by the <i>MMC-3</i> specification. This profile is used with devices that can read "DDCD-R specific structure." For a full list of the features supported with this profile, see the <i>MMC-3</i> specification.</td>
                </tr>
            
                <tr>
                    <td>ProfileDDCdRewritable</td>
                    <td>Indicates the profile named "DDCD-RW" by the <i>MMC-3</i> specification. This profile is used with devices that can read "DDCD-RW specific structure." For a full list of the features supported with this profile, see the <i>MMC-3</i> specification.</td>
                </tr>
            
                <tr>
                    <td>ProfileDvdPlusRWDualLayer</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ProfileDvdPlusRDualLayer</td>
                    <td>Reserved 0x002C - 0x003F</td>
                </tr>
            
                <tr>
                    <td>ProfileBDRom</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ProfileBDRSequentialWritable</td>
                    <td>BD-R 'SRM'</td>
                </tr>
            
                <tr>
                    <td>ProfileBDRRandomWritable</td>
                    <td>BD-R 'RRM'</td>
                </tr>
            
                <tr>
                    <td>ProfileBDRewritable</td>
                    <td>Reserved 0x0044 - 0x004F</td>
                </tr>
            
                <tr>
                    <td>ProfileHDDVDRom</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ProfileHDDVDRecordable</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ProfileHDDVDRam</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ProfileHDDVDRewritable</td>
                    <td>Reserved 0x0054 - 0x0057</td>
                </tr>
            
                <tr>
                    <td>ProfileHDDVDRDualLayer</td>
                    <td>Reserved 0x0059 - 0x0059</td>
                </tr>
            
                <tr>
                    <td>ProfileHDDVDRWDualLayer</td>
                    <td>Reserved 0x005B - 0xfffe</td>
                </tr>
            
                <tr>
                    <td>ProfileNonStandard</td>
                    <td>Indicates that the device does not conform to any profile.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddmmc.h (include Ntddcdrm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553816">FEATURE_DATA_PROFILE_LIST</a>
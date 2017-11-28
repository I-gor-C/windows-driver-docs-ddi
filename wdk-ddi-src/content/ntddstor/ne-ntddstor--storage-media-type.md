---
UID: NE.ntddstor._STORAGE_MEDIA_TYPE
title: STORAGE_MEDIA_TYPE
author: windows-driver-content
description: The STORAGE_MEDIA_TYPE enumeration is used in conjunction with the IOCTL_STORAGE_GET_MEDIA_TYPES_EX request to query the class driver for the types of media that a device supports.
old-location: storage\storage_media_type.htm
old-project: storage
ms.assetid: 70214b6e-92d2-418a-ad8a-8701df02fdc3
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
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
req.alt-api: STORAGE_MEDIA_TYPE
req.alt-loc: ntddstor.h
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

# STORAGE_MEDIA_TYPE enumeration



## -description
<p>The STORAGE_MEDIA_TYPE enumeration is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560563">IOCTL_STORAGE_GET_MEDIA_TYPES_EX</a> request to query the class driver for the types of media that a device supports.</p>


## -syntax

````
typedef enum _STORAGE_MEDIA_TYPE { 
  DDS_4mm             = 0x20,
  MiniQic             = 0x21,
  Travan              = 0x22,
  QIC                 = 0x23,
  MP_8mm              = 0x24,
  AME_8mm             = 0x25,
  AIT1_8mm            = 0x26,
  DLT                 = 0x27,
  NCTP                = 0x28,
  IBM_3480            = 0x29,
  IBM_3490E           = 0x2A,
  IBM_Magstar_3590    = 0x2B,
  IBM_Magstar_MP      = 0x2C,
  STK_DATA_D3         = 0x2D,
  SONY_DTF            = 0x2E,
  DV_6mm              = 0x2F,
  DMI                 = 0x30,
  SONY_D2             = 0x31,
  CLEANER_CARTRIDGE   = 0x32,
  CD_ROM              = 0x33,
  CD_R                = 0x34,
  CD_RW               = 0x35,
  DVD_ROM             = 0x36,
  DVD_R               = 0x37,
  DVD_RW              = 0x38,
  MO_3_RW             = 0x39,
  MO_5_WO             = 0x3A,
  MO_5_RW             = 0x3B,
  MO_5_LIMDOW         = 0x3C,
  PC_5_WO             = 0x3D,
  PC_5_RW             = 0x3E,
  PD_5_RW             = 0x3F,
  ABL_5_WO            = 0x40,
  PINNACLE_APEX_5_RW  = 0x41,
  SONY_12_WO          = 0x42,
  PHILIPS_12_WO       = 0x43,
  HITACHI_12_WO       = 0x44,
  CYGNET_12_WO        = 0x45,
  KODAK_14_WO         = 0x46,
  MO_NFR_525          = 0x47,
  NIKON_12_RW         = 0x48,
  IOMEGA_ZIP          = 0x49,
  IOMEGA_JAZ          = 0x4A,
  SYQUEST_EZ135       = 0x4B,
  SYQUEST_EZFLYER     = 0x4C,
  SYQUEST_SYJET       = 0x4D,
  AVATAR_F2           = 0x4E,
  MP2_8mm             = 0x4F,
  DST_S               = 0x50,
  DST_M               = 0x51,
  DST_L               = 0x52,
  VXATape_1           = 0x53,
  VXATape_2           = 0x54,
  STK_9840            = 0x55,
  LTO_Ultrium         = 0x56,
  LTO_Accelis         = 0x57,
  DVD_RAM             = 0x58,
  AIT_8mm             = 0x59,
  ADR_1               = 0x5A,
  ADR_2               = 0x5B,
  STK_9940            = 0x5C,
  SAIT                = 0x5D,
  VXATape             = 0x5E
} STORAGE_MEDIA_TYPE, *PSTORAGE_MEDIA_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DDS_4mm"></a><a id="dds_4mm"></a><a id="DDS_4MM"></a><b>DDS_4mm</b>

<dd>
<p>Indicates a DAT DDS1 or DDS2 tape device (all vendors).</p>
</dd>

### -field <a id="MiniQic"></a><a id="miniqic"></a><a id="MINIQIC"></a><b>MiniQic</b>

<dd>
<p>Indicates a mini-QIC tape device. </p>
</dd>

### -field <a id="Travan"></a><a id="travan"></a><a id="TRAVAN"></a><b>Travan</b>

<dd>
<p>Indicates a Travan TR-1, 2 or 3 tape device. </p>
</dd>

### -field <a id="QIC"></a><a id="qic"></a><b>QIC</b>

<dd>
<p>Indicates a QIC tape device. </p>
</dd>

### -field <a id="MP_8mm"></a><a id="mp_8mm"></a><a id="MP_8MM"></a><b>MP_8mm</b>

<dd>
<p>Indicates an 8mm Exabyte metal particle tape device. </p>
</dd>

### -field <a id="AME_8mm"></a><a id="ame_8mm"></a><a id="AME_8MM"></a><b>AME_8mm</b>

<dd>
<p>Indicates an 8mm Exabyte advanced metal tape device.</p>
</dd>

### -field <a id="AIT1_8mm"></a><a id="ait1_8mm"></a><a id="AIT1_8MM"></a><b>AIT1_8mm</b>

<dd>
<p>Indicates an 8mm Sony AIT tape device. </p>
</dd>

### -field <a id="DLT"></a><a id="dlt"></a><b>DLT</b>

<dd>
<p>Indicates a DLT compact IIIxt or IV tape device. </p>
</dd>

### -field <a id="NCTP"></a><a id="nctp"></a><b>NCTP</b>

<dd>
<p>Indicates a Philips NCTP tape device. </p>
</dd>

### -field <a id="IBM_3480"></a><a id="ibm_3480"></a><b>IBM_3480</b>

<dd>
<p>Indicates an IBM 3480 tape device. </p>
</dd>

### -field <a id="IBM_3490E"></a><a id="ibm_3490e"></a><b>IBM_3490E</b>

<dd>
<p>Indicates an IBM 3490E tape device.</p>
</dd>

### -field <a id="IBM_Magstar_3590"></a><a id="ibm_magstar_3590"></a><a id="IBM_MAGSTAR_3590"></a><b>IBM_Magstar_3590</b>

<dd>
<p>Indicates an IBM Magstar 3590 tape device. </p>
</dd>

### -field <a id="IBM_Magstar_MP"></a><a id="ibm_magstar_mp"></a><a id="IBM_MAGSTAR_MP"></a><b>IBM_Magstar_MP</b>

<dd>
<p>Indicates an IBM Magstar MP tape device. </p>
</dd>

### -field <a id="STK_DATA_D3"></a><a id="stk_data_d3"></a><b>STK_DATA_D3</b>

<dd>
<p>Indicates an STK data D3 tape device. </p>
</dd>

### -field <a id="SONY_DTF"></a><a id="sony_dtf"></a><b>SONY_DTF</b>

<dd>
<p>Indicates a Sony DTF tape device. </p>
</dd>

### -field <a id="DV_6mm"></a><a id="dv_6mm"></a><a id="DV_6MM"></a><b>DV_6mm</b>

<dd>
<p>Indicates a 6mm digital video tape device. </p>
</dd>

### -field <a id="DMI"></a><a id="dmi"></a><b>DMI</b>

<dd>
<p>Indicates a Exabyte DMI tape device and compatible devices. </p>
</dd>

### -field <a id="SONY_D2"></a><a id="sony_d2"></a><b>SONY_D2</b>

<dd>
<p>Indicates a Sony D2S or D2L tape device. </p>
</dd>

### -field <a id="CLEANER_CARTRIDGE"></a><a id="cleaner_cartridge"></a><b>CLEANER_CARTRIDGE</b>

<dd>
<p>Indicates a drive type that supports drive cleaners. </p>
</dd>

### -field <a id="CD_ROM"></a><a id="cd_rom"></a><b>CD_ROM</b>

<dd>
<p>Indicates a CD optical disk. </p>
</dd>

### -field <a id="CD_R"></a><a id="cd_r"></a><b>CD_R</b>

<dd>
<p>Indicates a CD-recordable (write once) optical disk. </p>
</dd>

### -field <a id="CD_RW"></a><a id="cd_rw"></a><b>CD_RW</b>

<dd>
<p>Indicates a CD-rewritable optical disk. </p>
</dd>

### -field <a id="DVD_ROM"></a><a id="dvd_rom"></a><b>DVD_ROM</b>

<dd>
<p>Indicates a DVD-ROM optical disk. </p>
</dd>

### -field <a id="DVD_R"></a><a id="dvd_r"></a><b>DVD_R</b>

<dd>
<p>Indicates a DVD-recordable (write once) optical disk. </p>
</dd>

### -field <a id="DVD_RW"></a><a id="dvd_rw"></a><b>DVD_RW</b>

<dd>
<p>Indicates a DVD-rewritable optical disk. </p>
</dd>

### -field <a id="MO_3_RW"></a><a id="mo_3_rw"></a><b>MO_3_RW</b>

<dd>
<p>Indicates a 3.5" rewritable MO optical disk. </p>
</dd>

### -field <a id="MO_5_WO"></a><a id="mo_5_wo"></a><b>MO_5_WO</b>

<dd>
<p>Indicates a MO 5.25" write once optical disk. </p>
</dd>

### -field <a id="MO_5_RW"></a><a id="mo_5_rw"></a><b>MO_5_RW</b>

<dd>
<p>Indicates a MO 5.25" rewritable (not LIMDOW) optical disk.</p>
</dd>

### -field <a id="MO_5_LIMDOW"></a><a id="mo_5_limdow"></a><b>MO_5_LIMDOW</b>

<dd>
<p>Indicates a MO 5.25" rewritable (LIMDOW) optical disk. </p>
</dd>

### -field <a id="PC_5_WO"></a><a id="pc_5_wo"></a><b>PC_5_WO</b>

<dd>
<p>Indicates a phase change 5.25" write once optical disk. </p>
</dd>

### -field <a id="PC_5_RW"></a><a id="pc_5_rw"></a><b>PC_5_RW</b>

<dd>
<p>Indicates a phase change 5.25" rewritable optical disk. </p>
</dd>

### -field <a id="PD_5_RW"></a><a id="pd_5_rw"></a><b>PD_5_RW</b>

<dd>
<p>Indicates a phase change dual rewritable optical disk. </p>
</dd>

### -field <a id="ABL_5_WO"></a><a id="abl_5_wo"></a><b>ABL_5_WO</b>

<dd>
<p>Indicates a ablative 5.25" write once optical disk. </p>
</dd>

### -field <a id="PINNACLE_APEX_5_RW"></a><a id="pinnacle_apex_5_rw"></a><b>PINNACLE_APEX_5_RW</b>

<dd>
<p>Indicates a pinnacle apex 4.6-GB rewritable optical disk.</p>
</dd>

### -field <a id="SONY_12_WO"></a><a id="sony_12_wo"></a><b>SONY_12_WO</b>

<dd>
<p>Indicates a Sony 12" write once optical disk. </p>
</dd>

### -field <a id="PHILIPS_12_WO"></a><a id="philips_12_wo"></a><b>PHILIPS_12_WO</b>

<dd>
<p>Indicates a Philips/LMS 12" write once optical disk. </p>
</dd>

### -field <a id="HITACHI_12_WO"></a><a id="hitachi_12_wo"></a><b>HITACHI_12_WO</b>

<dd>
<p>Indicates a Hitachi 12" write once optical disk. </p>
</dd>

### -field <a id="CYGNET_12_WO"></a><a id="cygnet_12_wo"></a><b>CYGNET_12_WO</b>

<dd>
<p>Indicates a Cygnet/ATG 12" write once optical disk. </p>
</dd>

### -field <a id="KODAK_14_WO"></a><a id="kodak_14_wo"></a><b>KODAK_14_WO</b>

<dd>
<p>Indicates a Kodak 14" write once optical disk. </p>
</dd>

### -field <a id="MO_NFR_525"></a><a id="mo_nfr_525"></a><b>MO_NFR_525</b>

<dd>
<p>Indicates a near field recording (Terastor) optical disk. </p>
</dd>

### -field <a id="NIKON_12_RW"></a><a id="nikon_12_rw"></a><b>NIKON_12_RW</b>

<dd>
<p>Indicates a Nikon 12" rewritable optical disk. </p>
</dd>

### -field <a id="IOMEGA_ZIP"></a><a id="iomega_zip"></a><b>IOMEGA_ZIP</b>

<dd>
<p>Indicates Iomega zip magnetic disk device. </p>
</dd>

### -field <a id="IOMEGA_JAZ"></a><a id="iomega_jaz"></a><b>IOMEGA_JAZ</b>

<dd>
<p>Indicates an Iomega Jaz magnetic disk device. </p>
</dd>

### -field <a id="SYQUEST_EZ135"></a><a id="syquest_ez135"></a><b>SYQUEST_EZ135</b>

<dd>
<p>Indicates a Syquest EZ135 magnetic disk device. </p>
</dd>

### -field <a id="SYQUEST_EZFLYER"></a><a id="syquest_ezflyer"></a><b>SYQUEST_EZFLYER</b>

<dd>
<p>Indicates a Syquest EzFlyer magnetic disk device. </p>
</dd>

### -field <a id="SYQUEST_SYJET"></a><a id="syquest_syjet"></a><b>SYQUEST_SYJET</b>

<dd>
<p>Indicates a Syquest SyJet magnetic disk device. </p>
</dd>

### -field <a id="AVATAR_F2"></a><a id="avatar_f2"></a><b>AVATAR_F2</b>

<dd>
<p>Indicates a 2.5" Floppy device. </p>
</dd>

### -field <a id="MP2_8mm"></a><a id="mp2_8mm"></a><a id="MP2_8MM"></a><b>MP2_8mm</b>

<dd>
<p>Indicates an 8mm Hitachi tape device. </p>
</dd>

### -field <a id="DST_S"></a><a id="dst_s"></a><b>DST_S</b>

<dd>
<p>Indicates a type DST Ampex small tape device. </p>
</dd>

### -field <a id="DST_M"></a><a id="dst_m"></a><b>DST_M</b>

<dd>
<p>Indicates a type DST Ampex medium tape device. </p>
</dd>

### -field <a id="DST_L"></a><a id="dst_l"></a><b>DST_L</b>

<dd>
<p>Indicates a type DST Ampex large tape device. </p>
</dd>

### -field <a id="VXATape_1"></a><a id="vxatape_1"></a><a id="VXATAPE_1"></a><b>VXATape_1</b>

<dd>
<p>Indicates an 8mm Ecrix tape device. </p>
</dd>

### -field <a id="VXATape_2"></a><a id="vxatape_2"></a><a id="VXATAPE_2"></a><b>VXATape_2</b>

<dd>
<p>Indicates an 8mm Ecrix tape device. </p>
</dd>

### -field <a id="STK_9840"></a><a id="stk_9840"></a><b>STK_9840</b>

<dd>
<p>Indicates an STK 9840 device. </p>
</dd>

### -field <a id="LTO_Ultrium"></a><a id="lto_ultrium"></a><a id="LTO_ULTRIUM"></a><b>LTO_Ultrium</b>

<dd>
<p>Indicates an IBM, HP, or Seagate LTO Ultrium device. </p>
</dd>

### -field <a id="LTO_Accelis"></a><a id="lto_accelis"></a><a id="LTO_ACCELIS"></a><b>LTO_Accelis</b>

<dd>
<p>Indicates an IBM, HP, or Seagate LTO Accelis</p>
</dd>

### -field <a id="DVD_RAM"></a><a id="dvd_ram"></a><b>DVD_RAM</b>

<dd>
<p>Indicates a DVD-RAM optical device. </p>
</dd>

### -field <a id="AIT_8mm"></a><a id="ait_8mm"></a><a id="AIT_8MM"></a><b>AIT_8mm</b>

<dd>
<p>Indicates an AIT2 or higher 8mm tape device. </p>
</dd>

### -field <a id="ADR_1"></a><a id="adr_1"></a><b>ADR_1</b>

<dd>
<p>Indicates an on-stream ADR media type device. </p>
</dd>

### -field <a id="ADR_2"></a><a id="adr_2"></a><b>ADR_2</b>

<dd>
<p>Indicates an on-stream ADR media type device. </p>
</dd>

### -field <a id="STK_9940"></a><a id="stk_9940"></a><b>STK_9940</b>

<dd>
<p>STK 9940</p>
</dd>

### -field <a id="SAIT"></a><a id="sait"></a><b>SAIT</b>

<dd>
<p>SAIT Tapes</p>
</dd>

### -field <a id="VXATape"></a><a id="vxatape"></a><a id="VXATAPE"></a><b>VXATape</b>

<dd>
<p>VXA (Ecrix 8mm) Tape</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552529">DEVICE_MEDIA_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554987">GET_MEDIA_TYPES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560563">IOCTL_STORAGE_GET_MEDIA_TYPES_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_MEDIA_TYPE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

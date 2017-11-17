---
UID: NS.ntddcdrm._CDROM_TOC_CD_TEXT_DATA_BLOCK
title: CDROM_TOC_CD_TEXT_DATA_BLOCK
author: windows-driver-content
description: This structure contains CD text descriptor data used in conjunction with the data in the CDROM_TOC_CD_TEXT_DATA structure.
old-location: storage\cdrom_toc_cd_text_data_block.htm
ms.assetid: 119386fe-1eff-4dac-b9d5-54baefcf6e12
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CDROM_TOC_CD_TEXT_DATA_BLOCK
req.alt-loc: ntddcdrm.h
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
ms.keywords: CDROM_TOC_CD_TEXT_DATA_BLOCK, CDROM_TOC_CD_TEXT_DATA_BLOCK, *PCDROM_TOC_CD_TEXT_DATA_BLOCK
req.iface: 
---

# CDROM_TOC_CD_TEXT_DATA_BLOCK structure



## -description
<p>This structure contains CD text descriptor data used in conjunction with the data in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551380">CDROM_TOC_CD_TEXT_DATA</a> structure. </p>


## -syntax

````
typedef struct _CDROM_TOC_CD_TEXT_DATA_BLOCK {
  UCHAR PackType;
  UCHAR TrackNumber  :7;
  UCHAR ExtensionFlag  :1;
  UCHAR SequenceNumber;
  UCHAR CharacterPosition  :4;
  UCHAR BlockNumber  :3;
  UCHAR Unicode  :1;
  union {
    UCHAR Text[12];
    WCHAR WText[6];
  };
  UCHAR CRC[2];
} CDROM_TOC_CD_TEXT_DATA_BLOCK, *PCDROM_TOC_CD_TEXT_DATA_BLOCK;
````


## -struct-fields
<dl>

### -field <b>PackType</b>

<dd>
<p>Indicates the type of pack data, as follows:</p>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_ALBUM_NAME_"></a><a id="cdrom_cd_text_pack_album_name_"></a>CDROM_CD_TEXT_PACK_ALBUM_NAME 

<dd>
<p>Title of album or track. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_PERFORMER_"></a><a id="cdrom_cd_text_pack_performer_"></a>CDROM_CD_TEXT_PACK_PERFORMER 

<dd>
<p>Names of the performers (in ASCII). </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_SONGWRITER_"></a><a id="cdrom_cd_text_pack_songwriter_"></a>CDROM_CD_TEXT_PACK_SONGWRITER 

<dd>
<p>Names of the songwriters (in ASCII). </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_COMPOSER_"></a><a id="cdrom_cd_text_pack_composer_"></a>CDROM_CD_TEXT_PACK_COMPOSER 

<dd>
<p>Names of the composers (in ASCII). </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_ARRANGER_"></a><a id="cdrom_cd_text_pack_arranger_"></a>CDROM_CD_TEXT_PACK_ARRANGER 

<dd>
<p>Names of the arrangers (in ASCII). </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_MESSAGES_"></a><a id="cdrom_cd_text_pack_messages_"></a>CDROM_CD_TEXT_PACK_MESSAGES 

<dd>
<p>Messages from content provider and/or artist (in ASCII). </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_DISC_ID"></a><a id="cdrom_cd_text_pack_disc_id"></a>CDROM_CD_TEXT_PACK_DISC_ID

<dd>
<p>Disc identification information. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_GENRE_"></a><a id="cdrom_cd_text_pack_genre_"></a>CDROM_CD_TEXT_PACK_GENRE 

<dd>
<p>Genre identification and information. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_TOC_INFO_"></a><a id="cdrom_cd_text_pack_toc_info_"></a>CDROM_CD_TEXT_PACK_TOC_INFO 

<dd>
<p>Table of contents information. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_TOC_INFO2_"></a><a id="cdrom_cd_text_pack_toc_info2_"></a>CDROM_CD_TEXT_PACK_TOC_INFO2 

<dd>
<p>Second table of contents information. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_UPC_EAN_"></a><a id="cdrom_cd_text_pack_upc_ean_"></a>CDROM_CD_TEXT_PACK_UPC_EAN 

<dd>
<p>UPC/EAN code of the album and ISRC code of each track. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CDROM_CD_TEXT_PACK_SIZE_INFO_"></a><a id="cdrom_cd_text_pack_size_info_"></a>CDROM_CD_TEXT_PACK_SIZE_INFO 

<dd>
<p>Size information for the block. </p>
</dd>
</dl>
</dd>

### -field <b>TrackNumber</b>

<dd>
<p>See specification <i>T10/1363-D Revision-02A</i>, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member. </p>
</dd>

### -field <b>ExtensionFlag</b>

<dd>
<p>Must be set to zero. </p>
</dd>

### -field <b>SequenceNumber</b>

<dd>
<p>See specification <i>T10/1363-D Revision-02A</i>, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member. </p>
</dd>

### -field <b>CharacterPosition</b>

<dd>
<p>See specification <i>T10/1363-D Revision-02A</i>, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member. </p>
</dd>

### -field <b>BlockNumber</b>

<dd>
<p>See specification <i>T10/1363-D Revision-02A</i>, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member.  </p>
</dd>

### -field <b>Unicode</b>

<dd>
<p>Indicates, when set to 1, that the text is stored in Unicode format. </p>
</dd>

### -field <b>Text</b>

<dd>
<p>Contains text descriptor data in the form of 8-bit ASCII characters.</p>
</dd>

### -field <b>WText</b>

<dd>
<p>Contains text descriptor data in the form of 16-bit (wide) characters.</p>
</dd>

### -field <b>CRC</b>

<dd>
<p>Contains the cyclic redundancy check.</p>
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
<dt>Ntddcdrm.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559367">IOCTL_CDROM_READ_TOC_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551366">CDROM_READ_TOC_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551380">CDROM_TOC_CD_TEXT_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20CDROM_TOC_CD_TEXT_DATA_BLOCK structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

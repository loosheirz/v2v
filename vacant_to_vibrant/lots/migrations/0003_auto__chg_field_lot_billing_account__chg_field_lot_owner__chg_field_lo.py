# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Lot.billing_account'
        db.alter_column(u'lots_lot', 'billing_account_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owners.BillingAccount'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Lot.owner'
        db.alter_column(u'lots_lot', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owners.Owner'], null=True, on_delete=models.SET_NULL))

        # Changing field 'Lot.parcel'
        db.alter_column(u'lots_lot', 'parcel_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parcels.Parcel'], null=True, on_delete=models.SET_NULL))

    def backwards(self, orm):

        # Changing field 'Lot.billing_account'
        db.alter_column(u'lots_lot', 'billing_account_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owners.BillingAccount'], null=True))

        # Changing field 'Lot.owner'
        db.alter_column(u'lots_lot', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['owners.Owner'], null=True))

        # Changing field 'Lot.parcel'
        db.alter_column(u'lots_lot', 'parcel_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parcels.Parcel'], null=True))

    models = {
        u'lots.lot': {
            'Meta': {'object_name': 'Lot'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'billing_account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['owners.BillingAccount']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['owners.Owner']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'parcel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parcels.Parcel']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'polygon': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'violations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['violations.Violation']", 'null': 'True', 'blank': 'True'})
        },
        u'owners.billingaccount': {
            'Meta': {'object_name': 'BillingAccount'},
            'external_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing_address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'mailing_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mailing_country': ('django.db.models.fields.CharField', [], {'default': "'USA'", 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'mailing_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'mailing_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'mailing_state_province': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'property_address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'owners.owner': {
            'Meta': {'object_name': 'Owner'},
            'billing_accounts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['owners.BillingAccount']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        },
        u'parcels.parcel': {
            'Meta': {'object_name': 'Parcel'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'basereg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapreg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'stcod': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'violations.violation': {
            'Meta': {'object_name': 'Violation'},
            'external_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'violation_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'violation_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['violations.ViolationLocation']"}),
            'violation_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['violations.ViolationType']"})
        },
        u'violations.violationlocation': {
            'Meta': {'object_name': 'ViolationLocation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'violations.violationtype': {
            'Meta': {'object_name': 'ViolationType'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'full_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'li_description': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['lots']